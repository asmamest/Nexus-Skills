
#!/usr/bin/env python3
"""Static structural validator for Nexus Skills.

This script intentionally does not execute any skill-provided code.
Requires Python 3.11+ and PyYAML.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print(
        "ERROR: PyYAML is required. Install with: "
        "python -m pip install -r requirements-dev.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
ALLOWED_CATEGORIES = {
    "software-engineering",
    "ai-engineering",
    "agentic-engineering",
    "devops-cloud",
    "security-quality",
}
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`]+)`")


class Validator:
    def __init__(self, root: Path = ROOT) -> None:
        self.root = root.resolve()
        self.skills_root = self.root / "skills"
        self.catalog = self.root / "CATALOG.md"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.skill_names: dict[str, Path] = {}
        self.skill_paths: set[str] = set()

    def error(self, path: Path, message: str) -> None:
        try:
            label = path.resolve().relative_to(self.root).as_posix()
        except ValueError:
            label = str(path)
        self.errors.append(f"{label}: {message}")

    def warn(self, path: Path, message: str) -> None:
        try:
            label = path.resolve().relative_to(self.root).as_posix()
        except ValueError:
            label = str(path)
        self.warnings.append(f"{label}: {message}")

    def validate(self) -> int:
        if not self.skills_root.is_dir():
            self.error(self.skills_root, "skills/ directory is missing")
            self.print_report()
            return 1

        skill_files = sorted(self.skills_root.glob("*/*/SKILL.md"))
        if not skill_files:
            self.error(
                self.skills_root,
                "no skills found; expected skills/<category>/<skill>/SKILL.md",
            )

        for skill_file in skill_files:
            self.validate_skill(skill_file)

        self.validate_catalog(skill_files)
        self.print_report()
        return 1 if self.errors else 0

    def validate_skill(self, skill_file: Path) -> None:
        rel = skill_file.relative_to(self.root)
        parts = rel.parts

        if len(parts) != 4:
            self.error(
                skill_file,
                "must be located at skills/<category>/<skill>/SKILL.md",
            )
            return

        category, directory_name = parts[1], parts[2]

        if category not in ALLOWED_CATEGORIES:
            self.error(
                skill_file,
                f"unknown category '{category}'; allowed: "
                f"{', '.join(sorted(ALLOWED_CATEGORIES))}",
            )

        if directory_name.startswith("."):
            self.error(skill_file, "skill directory must not start with a dot")

        if not NAME_RE.fullmatch(directory_name) or len(directory_name) > MAX_NAME:
            self.error(
                skill_file,
                "directory name must be lowercase kebab-case "
                "and at most 64 characters",
            )

        try:
            # utf-8-sig consumes a UTF-8 BOM if one is present.
            content = skill_file.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            self.error(skill_file, f"cannot read as UTF-8: {exc}")
            return

        # Tolerate blank lines before frontmatter, but not arbitrary text.
        content = content.lstrip("\r\n")

        frontmatter, body = self.parse_frontmatter(skill_file, content)
        if frontmatter is None:
            return

        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not isinstance(name, str) or not name.strip():
            self.error(
                skill_file,
                "'name' is required and must be a non-empty string",
            )
        else:
            if name != name.strip():
                self.error(
                    skill_file,
                    "'name' must not contain leading/trailing whitespace",
                )
            if len(name) > MAX_NAME or not NAME_RE.fullmatch(name):
                self.error(
                    skill_file,
                    "'name' must be lowercase kebab-case and at most 64 characters",
                )
            if name != directory_name:
                self.error(
                    skill_file,
                    f"name '{name}' must match directory '{directory_name}'",
                )
            if name in self.skill_names:
                self.error(
                    skill_file,
                    f"duplicate skill name '{name}' also used by "
                    f"{self.skill_names[name]}",
                )
            else:
                self.skill_names[name] = skill_file
            self.skill_paths.add(rel.as_posix())

        if not isinstance(description, str) or not description.strip():
            self.error(
                skill_file,
                "'description' is required and must be a non-empty string",
            )
        else:
            if len(description) > MAX_DESCRIPTION:
                self.error(
                    skill_file,
                    f"'description' exceeds {MAX_DESCRIPTION} characters",
                )
            if description != description.strip():
                self.error(
                    skill_file,
                    "'description' must not contain leading/trailing whitespace",
                )
            if "<" in description or ">" in description:
                self.error(
                    skill_file,
                    "'description' must not contain angle brackets",
                )

        license_value = frontmatter.get("license")
        if license_value is not None and not isinstance(license_value, str):
            self.error(skill_file, "'license' must be a string when provided")

        compatibility = frontmatter.get("compatibility")
        if compatibility is not None:
            if not isinstance(compatibility, str) or not compatibility.strip():
                self.error(
                    skill_file,
                    "'compatibility' must be a non-empty string when provided",
                )
            elif len(compatibility) > 500:
                self.error(
                    skill_file,
                    "'compatibility' exceeds 500 characters",
                )

        metadata = frontmatter.get("metadata")
        if metadata is not None:
            if not isinstance(metadata, dict):
                self.error(
                    skill_file,
                    "'metadata' must be a mapping of string keys to string values",
                )
            elif any(
                not isinstance(key, str) or not isinstance(value, str)
                for key, value in metadata.items()
            ):
                self.error(
                    skill_file,
                    "all 'metadata' keys and values must be strings",
                )

        allowed_tools = frontmatter.get("allowed-tools")
        if allowed_tools is not None and not isinstance(allowed_tools, str):
            self.error(
                skill_file,
                "'allowed-tools' must be a space-separated string "
                "in portable skills",
            )

        if not body.strip():
            self.error(
                skill_file,
                "instruction body after frontmatter must not be empty",
            )

        if len(content.encode("utf-8")) > 256 * 1024:
            self.error(
                skill_file,
                "SKILL.md exceeds 256 KiB; keep instructions concise "
                "and move detail to references/",
            )

        skill_dir = skill_file.parent
        markdown_files = sorted(set([skill_file, *skill_dir.rglob("*.md")]))

        for markdown_file in markdown_files:
            self.validate_markdown_links(markdown_file, skill_dir)

        for candidate in skill_dir.rglob("*"):
            if (
                candidate.is_file()
                and candidate.name.lower() == "skill.md"
                and candidate != skill_file
            ):
                self.error(
                    candidate,
                    "a skill directory must contain only one SKILL.md manifest",
                )

    def parse_frontmatter(
        self, path: Path, content: str
    ) -> tuple[dict[str, Any] | None, str]:
        # Accept Unix and Windows line endings.
        normalized = content.replace("\r\n", "\n").replace("\r", "\n")

        if not normalized.startswith("---\n"):
            self.error(
                path,
                "file must start with YAML frontmatter opened by ---",
            )
            return None, ""

        lines = normalized.splitlines()
        closing = None

        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                closing = index
                break

        if closing is None:
            self.error(path, "YAML frontmatter closing --- is missing")
            return None, ""

        raw = "\n".join(lines[1:closing])

        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            self.error(path, f"invalid YAML frontmatter: {exc}")
            return None, ""

        body = "\n".join(lines[closing + 1:])

        if not isinstance(data, dict):
            self.error(path, "frontmatter must parse to a YAML mapping")
            return None, body

        return data, body

    def validate_markdown_links(
        self, markdown_file: Path, skill_dir: Path
    ) -> None:
        try:
            text = markdown_file.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            self.error(
                markdown_file,
                f"cannot read Markdown file as UTF-8: {exc}",
            )
            return

        text_without_code = INLINE_CODE_RE.sub("", text)

        for target in MARKDOWN_LINK_RE.findall(text_without_code):
            target = target.strip()

            if not target or target.startswith(
                ("https://", "http://", "mailto:", "#", "data:")
            ):
                continue

            target = target.split()[0].split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue

            target_path = (markdown_file.parent / target).resolve()

            try:
                target_path.relative_to(skill_dir.resolve())
            except ValueError:
                self.error(
                    markdown_file,
                    f"local link escapes the skill directory: {target}",
                )
                continue

            if not target_path.exists():
                self.error(markdown_file, f"broken local link: {target}")

    def validate_catalog(self, skill_files: list[Path]) -> None:
        if not self.catalog.is_file():
            self.error(self.catalog, "CATALOG.md is missing")
            return

        try:
            catalog_text = self.catalog.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as exc:
            self.error(self.catalog, f"cannot read as UTF-8: {exc}")
            return

        for skill_file in skill_files:
            rel = skill_file.relative_to(self.root).as_posix()
            if rel not in catalog_text:
                self.error(
                    self.catalog,
                    f"missing catalog entry/path for {rel}",
                )

        for listed in re.findall(
            r"`(skills/[^`]+/SKILL\.md)`", catalog_text
        ):
            target = (self.root / listed).resolve()
            if not target.is_file():
                self.error(
                    self.catalog,
                    f"catalog points to missing skill manifest: {listed}",
                )

    def print_report(self) -> None:
        for warning in self.warnings:
            print(f"WARNING: {warning}")

        for error in self.errors:
            print(f"ERROR: {error}")

        if self.errors:
            print(
                f"\nValidation failed: {len(self.errors)} error(s), "
                f"{len(self.warnings)} warning(s)."
            )
        else:
            print(
                f"Validation passed: {len(self.skill_names)} skill(s), "
                f"{len(self.warnings)} warning(s)."
            )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Nexus Skills structure and catalog consistency."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root (defaults to the parent of scripts/).",
    )
    args = parser.parse_args()
    validator = Validator(args.root)
    return validator.validate()


if __name__ == "__main__":
    raise SystemExit(main())
