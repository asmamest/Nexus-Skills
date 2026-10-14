import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import Validator  # noqa: E402


class ValidatorTests(unittest.TestCase):
    def make_repo(self, skill_name="sample-skill", description="Do a sample task when requested.", body="# Instructions\n\nDo the task carefully.\n"):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        skill_dir = root / "skills" / "software-engineering" / skill_name
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            f"---\nname: {skill_name}\ndescription: {description}\n---\n\n{body}",
            encoding="utf-8",
        )
        (root / "CATALOG.md").write_text(
            f"# Catalog\n\n`{skill_name}`\n\n`skills/software-engineering/{skill_name}/SKILL.md`\n",
            encoding="utf-8",
        )
        return temp, root

    def test_valid_skill_passes(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        self.assertEqual(Validator(root).validate(), 0)

    def test_name_must_match_directory(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        manifest = root / "skills/software-engineering/sample-skill/SKILL.md"
        manifest.write_text(
            "---\nname: different-name\ndescription: Do a sample task.\n---\n\nBody.\n",
            encoding="utf-8",
        )
        self.assertEqual(Validator(root).validate(), 1)

    def test_broken_local_link_fails(self):
        temp, root = self.make_repo(body="# Instructions\n\nSee [missing](references/not-here.md).\n")
        self.addCleanup(temp.cleanup)
        self.assertEqual(Validator(root).validate(), 1)

    def test_missing_catalog_path_fails(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        (root / "CATALOG.md").write_text("# Catalog\n", encoding="utf-8")
        self.assertEqual(Validator(root).validate(), 1)

    def test_bad_frontmatter_fails(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        manifest = root / "skills/software-engineering/sample-skill/SKILL.md"
        manifest.write_text("No frontmatter here.\n", encoding="utf-8")
        self.assertEqual(Validator(root).validate(), 1)


    def test_invalid_compatibility_length_fails(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        manifest = root / "skills/software-engineering/sample-skill/SKILL.md"
        manifest.write_text(
            "---\nname: sample-skill\ndescription: Do a sample task.\ncompatibility: "
            + ("x" * 501) + "\n---\n\nBody.\n",
            encoding="utf-8",
        )
        self.assertEqual(Validator(root).validate(), 1)



if __name__ == "__main__":
    unittest.main()
