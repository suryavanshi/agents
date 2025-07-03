# Agent Development Guidelines for Agent-Driven Forge

This document provides guidelines for AI agents working on or with the "Agent-Driven Forge" codebase.

## General Principles

1.  **Modularity:** Each agent should be self-contained within its respective directory (e.g., `orchestrator/`, `architect/`). Core logic for an agent should reside primarily within its Python file (e.g., `orchestrator.py`).
2.  **Clear Interfaces:** Agents should communicate through well-defined interfaces or methods. The `Orchestrator` agent is typically the central hub for communication, but direct interaction between specialized agents might occur if defined by the `Orchestrator`.
3.  **Idempotency (where applicable):** Operations, especially those performed by `CoderAgents` or `DevOpsAgent`, should be designed to be idempotent where possible. For example, re-applying a configuration should not cause errors.
4.  **Extensibility:** Design agent capabilities with extensibility in mind. New functionalities should be addable without requiring major overhauls of existing agent logic.
5.  **Logging and Reporting:** Each agent should provide clear logging of its actions and decisions. This is crucial for the `ICEInterface` to display a coherent activity stream and for human oversight.

## Agent-Specific Guidelines

### All Agents

*   **Initialization:** Each agent should have an `__init__` method that clearly states its initialization (e.g., printing a message like "`<AgentName> Agent initialized`").
*   **Task-Specific Methods:** Implement distinct methods for primary responsibilities (e.g., `architect.design_system()`, `coder_agent.write_code()`).
*   **Return Values:** Methods that produce artifacts (code, configurations, reports) should return them in a structured format (e.g., dictionaries, strings, lists of objects).

### Orchestrator Agent (`orchestrator/orchestrator.py`)

*   Responsible for parsing human developer's high-level requirements.
*   Must break down these requirements into actionable tasks for other agents.
*   Manages the overall workflow, ensuring tasks are delegated correctly and in the right sequence.
*   Collects results/artifacts from other agents and reports progress to the `ICEInterface`.

### Architect Agent (`architect/architect.py`)

*   Takes a project brief from the `Orchestrator`.
*   Defines and returns a clear system architecture, including:
    *   Technology stack (e.g., programming languages, frameworks, databases).
    *   Database schema (if applicable).
    *   API contracts (if applicable).
    *   High-level directory and file structure for the project being built.

### Coder Agents (`coder_agents/coder_agent.py`)

*   Receive specific, well-defined coding tasks from the `Orchestrator`.
*   Must adhere to the specifications provided by the `Architect` (e.g., language, framework, file locations).
*   Generated code should be returned as a string or written to a specified file path.
*   If multiple `CoderAgents` are active, the `Orchestrator` will manage their parallel tasks.

### QA & Debugger Agent (`qa_debugger_agent/qa_debugger.py`)

*   Can perform static code analysis.
*   Can write and execute unit and integration tests (this may involve generating test files).
*   Identifies bugs and can attempt automated fixes or report them back to the `Orchestrator`.

### DevOps Agent (`devops_agent/devops.py`)

*   Generates `Dockerfiles` based on project specifications.
*   Configures CI/CD pipelines (e.g., generating GitHub Actions workflow files).
*   Generates deployment scripts for various platforms (e.g., Kubernetes YAML, Terraform).

### Refactor Agent (`refactor_agent/refactor.py`)

*   Scans the codebase (as directed by the `Orchestrator`) for potential improvements.
*   Suggests refactors related to performance, readability, and best practices.
*   Can automatically apply refactors, but changes should be clearly logged and ideally version-controlled.

## Intelligent Command Environment (ICE) (`intelligent_command_environment/ice_interface.py`)

*   While not an "agent" in the same vein, the ICE is the primary human-AI interaction point.
*   It should clearly display the activity stream from all agents.
*   It must be able to parse natural language commands from the developer and relay them to the `Orchestrator`.

## Future Development

*   When adding new agents or significant capabilities, update this `AGENTS.md` file.
*   Consider adding programmatic checks (e.g., a linting script for agent code structure) if the system grows in complexity.

This file helps ensure that as the project evolves, especially if different AI agents (or human developers guided by AI) contribute, there's a consistent approach to development.
