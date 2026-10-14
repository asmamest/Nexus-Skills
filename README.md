# Nexus Skills

Community-built, reusable skills for Claude Code, Codex, and AI coding agents.

Nexus Skills is an open-source library of practical skills that help AI coding agents perform engineering tasks through structured instructions, repeatable workflows, and explicit quality checks.

The goal is simple: make useful engineering knowledge reusable, discoverable, and accessible to everyone.

## Why Nexus Skills?

Good agent instructions should be more than one-off prompts. They should describe a task, guide execution, account for edge cases, and define how to verify the result.

Nexus Skills brings these workflows together in a shared, community-maintained library.

- **Open:** Anyone can propose a skill or improve an existing one.
- **Reusable:** Skills follow a consistent, portable directory structure.
- **Practical:** Skills focus on real engineering tasks and verifiable outcomes.
- **Transparent:** Contributions are reviewed through public pull requests.
- **Agent-friendly:** Skills target Claude Code, Codex, and other compatible agents where supported.

## Categories

Skills are organized by their primary engineering domain.

| Category | Scope |
| --- | --- |
| `software-engineering` | Code review, debugging, refactoring, testing, and architecture |
| `ai-engineering` | RAG, LLM evaluation, model development, and inference |
| `agentic-engineering` | Agent workflows, MCP development, tool use, and evaluation |
| `devops-cloud` | CI/CD, containers, deployment, cloud infrastructure, and monitoring |
| `security-quality` | Secure coding, threat modeling, dependency auditing, and quality assurance |

Browse the [`skills/`](skills/) directory to explore available skills.

## Repository structure

```
Nexus-Skills/
├── skills/
│   ├── software-engineering/
│   ├── ai-engineering/
│   ├── agentic-engineering/
│   ├── devops-cloud/
│   └── security-quality/
├── templates/
│   └── SKILL.md
├── CONTRIBUTING.md
├── CATALOG.md
└── README.md
```

Each skill lives in its own directory and contains a `SKILL.md` file. Optional references, scripts, and assets may be included when they provide meaningful value.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/asmamest/Nexus-Skills.git
cd Nexus-Skills
```

### 2. Choose a skill

Browse [`skills/`](skills/) and select the skill you want to use. The examples below use `code-review`; replace the source path with the skill you choose.

### 3. Install for Claude Code

On macOS, Linux, or WSL:

```bash
mkdir -p ~/.claude/skills
cp -R skills/software-engineering/code-review \
  ~/.claude/skills/code-review
```

For project-specific use, copy the skill into:

```
your-project/.claude/skills/code-review/
```

### 4. Install for Codex

On macOS, Linux, or WSL:

```bash
mkdir -p ~/.agents/skills
cp -R skills/software-engineering/code-review \
  ~/.agents/skills/code-review
```

For project-specific use, copy the skill into:

```
your-project/.agents/skills/code-review/
```

Follow the official documentation for your agent and version if its skill-discovery behavior differs from these defaults.

- [Claude Code skills documentation](https://docs.anthropic.com/en/docs/claude-code)
- [OpenAI Codex documentation](https://platform.openai.com/docs/)

> **Note:** Nexus Skills is a library, not an installer or execution engine. Review a skill's instructions and any included scripts before using them.

## Creating a skill

1. Choose a specific, reusable engineering task.
2. Create a directory under the appropriate category in `skills/`.
3. Add a `SKILL.md` following [`templates/SKILL.md`](templates/SKILL.md).
4. Include clear instructions, realistic examples, and verification steps.
5. Test the skill with its intended agent or agents.
6. Update [`CATALOG.md`](CATALOG.md) and submit a pull request.

## Contributing

Contributions are welcome, whether you are adding a new skill, improving documentation, fixing an issue, or testing an existing workflow.

Before submitting a contribution, read [`CONTRIBUTING.md`](CONTRIBUTING.md).

All contributions should be practical, clearly documented, safe to use, and respectful of third-party licenses.

### Quality over quantity

Nexus Skills prioritizes useful, maintainable workflows over the number of published skills.

Compatibility should reflect actual testing, not assumptions based on file format alone. Skills that have not been tested with a particular agent should say so.

## License

Nexus Skills is distributed under the MIT License, subject to the terms of that license and applicable rights in third-party materials.

By contributing, you agree that your contribution may be distributed under the repository's license.

---

**Built in the open. Improved by the community.**
