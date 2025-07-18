# versusMonster AVPS (Automated Video Podcast System)

This repository contains the source code for the versusMonster Automated Video Podcast System (AVPS). The goal of this project is to transform markdown scripts into complete, YouTube-ready podcast episodes with minimal manual intervention.

## 🚀 Getting Started

To get started with this project, please refer to the following documents:

*   **[Development Workflow Guide](.ai-context/WORKFLOW_GUIDE.md):** This document provides a comprehensive overview of the development process, from task management to implementation and validation.
*   **[Project Requirements Document (PRD)](docs/specifications/PRD.md):** This document outlines the project's goals, requirements, and success criteria.
*   **[AI Agent Guides](.ai-context/):** This directory contains specific instructions for interacting with the various AI assistants used in this project, including the `.claude/commands/` directory which houses the executable command files for the Claude AI.

### 🛠️ Available AI Commands

Key commands for managing the development workflow, often executed by AI agents via `.claude/commands/*.md` files:

*   **`@next-task`** - Get the next available task and create implementation plan
*   **`@finalize-task`** - Complete current task and update Notion
*   **`@update-prd`** - Sync Notion task completion status with PRD.md component progress
*   **`@orient`** - Get oriented in the project and see next best actions

## 📂 Codebase Structure

Here is a simplified visual outline of the project's directory structure. For a more detailed breakdown, please see the **[Codebase Structure Document](docs/specifications/codebase_structure.md)**.

```
/
├── .ai-context/     # AI agent context and guides
├── config/          # Project configuration files
├── docs/            # Project documentation
├── output/          # Generated output (audio, video, etc.)
├── src/             # Main source code
├── tests/           # Test files and reference data
├── ...              # Other project files
```

## 📋 Current Status

The project is currently in active development. For the latest status on each component, please refer to the **[Project Requirements Document (PRD)](docs/specifications/PRD.md)**.

## 🤖 AI-Assisted Development

This project leverages a multi-agent AI team to accelerate development. For more information on the different AI assistants and their roles, please see the guides in the **[.ai-context](.ai-context/)** directory.

## 🤝 Contributing

We welcome contributions to this project. If you are interested in contributing, please start by reading the **[Development Workflow Guide](.ai-context/WORKFLOW_GUIDE.md)**.