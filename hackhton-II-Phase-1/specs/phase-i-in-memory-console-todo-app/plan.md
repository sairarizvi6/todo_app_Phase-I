# Implementation Plan: Phase I – In-Memory Python Console Todo App

**Branch**: `phase-i-in-memory-console-todo-app` | **Date**: 2026-01-02 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/sp.specify`

## Summary

Build a simple command-line todo application that stores tasks in memory using a layered architecture with clear separation of concerns. The application provides five core operations: add, view, update, delete, and mark complete. Target audience is beginner to intermediate Python developers, emphasizing clean code principles and modular design for future extensibility.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: UV (package manager), click or argparse (CLI framework)
**Storage**: In-memory list/dict (no persistence)
**Testing**: pytest
**Target Platform**: Linux/macOS/Windows console
**Project Type**: Single-process console application
**Performance Goals**: <100ms per operation (in-memory, no I/O)
**Constraints**: Console-only, no database, no web/AI/cloud features
**Scale/Scope**: Single user, small todo lists (tens to hundreds of items)

## Constitution Check

| Principle | Check | Status |
|-----------|-------|--------|
| I. Correctness Before Complexity | Simple in-memory implementation, testable logic | ✅ Pass |
| II. Incremental Evolution | Phase I isolated, foundation for future phases | ✅ Pass |
| III. Simplicity and Clarity | Layered architecture, clear module separation | ✅ Pass |
| IV. Cloud-Native Best Practices | N/A for Phase I (console app) | ✅ Pass |
| V. Purposeful AI Integration | N/A for Phase I (no AI features) | ✅ Pass |

## Project Structure

### Documentation (this feature)

```text
specs/phase-i-in-memory-console-todo-app/
├── plan.md              # This file
├── spec.md              # Feature specification
└── tasks.md             # To be created by /sp.tasks
```

### Source Code (repository root)

```text
todo/
├── __init__.py
├── models.py            # Todo entity, TodoStore (Model Layer)
├── service.py           # TodoService (Service Layer)
├── cli.py               # Console UI, argument parsing (UI Layer)
└── main.py              # Entry Point
pyproject.toml           # UV configuration
tests/
├── __init__.py
├── test_models.py       # Unit tests for models
├── test_service.py      # Unit tests for service layer
└── test_cli.py          # Integration tests for CLI
```

**Structure Decision**: Single project with layered architecture:
- **Model Layer** (`models.py`): Todo data class and in-memory TodoStore
- **Service Layer** (`service.py`): Business logic for CRUD operations
- **UI Layer** (`cli.py`): Console input/output, command routing
- **Entry Point** (`main.py`): Application startup

### Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│ User Input (CLI arguments)                                  │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│ UI Layer (cli.py) - Parse arguments, format output          │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│ Service Layer (service.py) - Business logic orchestration   │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│ Model Layer (models.py) - Todo data, TodoStore in-memory    │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Phases

### Phase 1: Foundation
1. Create project structure and `pyproject.toml` with UV
2. Implement `Todo` dataclass in `models.py`
3. Implement `TodoStore` with in-memory list
4. Implement basic `TodoService` wrapping `TodoStore`

### Phase 2: CLI Interface
1. Set up click/argparse CLI in `cli.py`
2. Implement `add` command
3. Implement `list` command
4. Wire up entry point in `main.py`

### Phase 3: CRUD Operations
1. Implement `complete` command
2. Implement `update` command
3. Implement `delete` command
4. Add input validation and error handling

### Phase 4: Testing
1. Write unit tests for `TodoStore`
2. Write unit tests for `TodoService`
3. Write integration tests for CLI commands
4. Verify all 5 features work correctly

## Complexity Tracking

> No constitution violations detected. Implementation follows all principles with minimal complexity appropriate for Phase I.

## Open Questions

- CLI framework preference: `click` or `argparse`? (Both work; recommend `click` for cleaner command definitions)
- ID generation: Sequential integers starting at 1, or UUIDs? (Recommend sequential for beginner-friendly UX)

Would you like to proceed with `/sp.tasks` to generate testable tasks?
