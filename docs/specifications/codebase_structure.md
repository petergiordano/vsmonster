# Codebase Structure

This document provides a visual overview of the directory structure for the versusMonster AVPS project.

```
/
├── .ai-context/
│   ├── AI_CONTEXT.md
│   └── WORKFLOW_GUIDE.md
├── .ai-rules/
│   └── 01_create-prd.md
├── .claude/
│   ├── settings.local.json
│   └── commands/
├── .git/
├── .github/
├── .mypy_cache/
├── .pytest_cache/
├── .vscode/
├── archive/
├── assets/
│   ├── branding/
│   ├── images/
│   ├── music/
│   ├── sfx/
│   └── templates/
├── config/
│   ├── .env.example
│   ├── .flake8
│   ├── .markdownlint.json
│   ├── config.json
│   ├── environment.yml
│   ├── mypy.ini
│   ├── notion-database-schema.json
│   └── pytest.ini
├── docs/
│   ├── architecture/
│   ├── examples/
│   ├── setup/
│   └── specifications/
│       ├── PRD.md
│       ├── codebase_structure.md
│       └── ...
├── output/
│   ├── audio/
│   ├── json/
│   ├── videos/
│   └── voices/
├── src/
│   ├── __init__.py
│   ├── cost_reporter.py
│   ├── parser.py
│   ├── voice_gen.py
│   └── utils/
│       └── __init__.py
├── tests/
│   └── reference/
├── tools/
│   ├── process_episode.py
│   ├── setup_validation.py
│   └── update_prd_status.py
├── venv/
├── .gitignore
├── ABOUT_JULES.md
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── JULES.md
├── pyproject.toml
├── README.md
├── requirements.txt
└── TODO.md
```