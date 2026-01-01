# Tasks: Phase I – In-Memory Python Console Todo App

**Input**: Design documents from `/specs/phase-i-in-memory-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required)

**Tests**: Included - unit tests for models, service layer, and CLI integration

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `pyproject.toml` with UV configuration for Python 3.13+, click, pytest
- [X] T002 Create `todo/__init__.py` package file
- [X] T003 Create `tests/__init__.py` package file
- [X] T004 [P] Create `.python-version` file specifying Python 3.13+

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data models that ALL user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 [P] Implement `Todo` dataclass in `todo/models.py` with id, text, completed fields
- [X] T006 [P] Implement `TodoStore` class in `todo/models.py` with in-memory list storage
- [X] T007 [P] Implement `TodoService` class in `todo/service.py` wrapping `TodoStore`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Items (Priority: P1) MVP

**Goal**: Users can add new todo items to track tasks

**Independent Test**: Run `python -m todo add "Buy groceries"` and verify todo is stored in memory

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T008 [P] [US1] Unit test for TodoStore.add() in `tests/test_models.py`
- [X] T009 [P] [US1] Unit test for TodoService.add_todo() in `tests/test_service.py`
- [X] T010 [US1] CLI integration test for `add` command in `tests/test_cli.py`

### Implementation for User Story 1

- [X] T011 [US1] Implement `add` CLI command in `todo/cli.py`
- [X] T012 [US1] Connect CLI `add` command to TodoService in `todo/cli.py`
- [X] T013 [US1] Add input validation (non-empty text) and error handling in `todo/cli.py`

**Checkpoint**: User Story 1 complete and testable - `python -m todo add "Task"` works

---

## Phase 4: User Story 2 - View Todo Items (Priority: P1)

**Goal**: Users can see all their todo items with status

**Independent Test**: Run `python -m todo list` and verify all todos are displayed correctly

### Tests for User Story 2

- [X] T014 [P] [US2] Unit test for TodoStore.get_all() in `tests/test_models.py`
- [X] T015 [P] [US2] Unit test for TodoService.get_todos() in `tests/test_service.py`
- [X] T016 [US2] CLI integration test for `list` command in `tests/test_cli.py`

### Implementation for User Story 2

- [X] T017 [US2] Implement `list` CLI command in `todo/cli.py`
- [X] T018 [US2] Connect CLI `list` command to TodoService in `todo/cli.py`
- [X] T019 [US2] Add empty state message handling in `todo/cli.py`

**Checkpoint**: User Story 2 complete - `python -m todo list` works with proper formatting

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P1)

**Goal**: Users can mark todos as complete to track progress

**Independent Test**: Run `python -m todo complete 1` and verify todo status changes to complete

### Tests for User Story 3

- [X] T020 [P] [US3] Unit test for TodoStore.complete() in `tests/test_models.py`
- [X] T021 [P] [US3] Unit test for TodoService.complete_todo() in `tests/test_service.py`
- [X] T022 [US3] CLI integration test for `complete` command in `tests/test_cli.py`

### Implementation for User Story 3

- [X] T023 [US3] Implement `complete` CLI command in `todo/cli.py`
- [X] T024 [US3] Connect CLI `complete` command to TodoService in `todo/cli.py`
- [X] T025 [US3] Add idempotent handling (already complete case) in `todo/service.py`

**Checkpoint**: User Story 3 complete - `python -m todo complete 1` works with proper messaging

---

## Phase 6: User Story 4 - Update Todo Items (Priority: P2)

**Goal**: Users can update todo text to correct mistakes or refine descriptions

**Independent Test**: Run `python -m todo update 1 "New description"` and verify text is updated

### Tests for User Story 4

- [X] T026 [P] [US4] Unit test for TodoStore.update() in `tests/test_models.py`
- [X] T027 [P] [US4] Unit test for TodoService.update_todo() in `tests/test_service.py`
- [X] T028 [US4] CLI integration test for `update` command in `tests/test_cli.py`

### Implementation for User Story 4

- [X] T029 [US4] Implement `update` CLI command in `todo/cli.py`
- [X] T030 [US4] Connect CLI `update` command to TodoService in `todo/cli.py`
- [X] T031 [US4] Add error handling for non-existent IDs in `todo/cli.py`

**Checkpoint**: User Story 4 complete - `python -m todo update 1 "New text"` works

---

## Phase 7: User Story 5 - Delete Todo Items (Priority: P2)

**Goal**: Users can remove todos that are no longer relevant

**Independent Test**: Run `python -m todo delete 1` and verify todo is removed

### Tests for User Story 5

- [X] T032 [P] [US5] Unit test for TodoStore.delete() in `tests/test_models.py`
- [X] T033 [P] [US5] Unit test for TodoService.delete_todo() in `tests/test_service.py`
- [X] T034 [US5] CLI integration test for `delete` command in `tests/test_cli.py`

### Implementation for User Story 5

- [X] T035 [US5] Implement `delete` CLI command in `todo/cli.py`
- [X] T036 [US5] Connect CLI `delete` command to TodoService in `todo/cli.py`
- [X] T037 [US5] Add error handling for non-existent IDs in `todo/cli.py`

**Checkpoint**: User Story 5 complete - `python -m todo delete 1` works

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T038 [P] Run all pytest tests and ensure 100% pass rate
- [X] T039 Verify all 5 features work correctly via manual testing
- [X] T040 [P] Add docstrings to all public functions and classes
- [X] T041 Create project README with setup and usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|------------|--------|
| Setup (1) | None | Foundational |
| Foundational (2) | Setup | All user stories |
| US1-3 (3-5) | Foundational | US4-5 |
| US4-5 (6-7) | Foundational, US1-3 | Polish |
| Polish (8) | All user stories | None |

### User Story Dependencies

- **User Story 1 (Add)**: Can start after Foundational - No other dependencies
- **User Story 2 (View)**: Can start after Foundational - No other dependencies
- **User Story 3 (Complete)**: Can start after Foundational - No other dependencies
- **User Story 4 (Update)**: Can start after Foundational - Integrates with US1 components
- **User Story 5 (Delete)**: Can start after Foundational - Integrates with US1 components

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models (T005-T007) before all stories
- CLI commands depend on corresponding service methods
- Story complete before moving to next priority (for MVP delivery)

### Parallel Opportunities

| Phase | Parallel Tasks |
|-------|----------------|
| Setup | T001-T004 (all different files) |
| Foundational | T005-T007 (all different files) |
| US1 | T008-T010 (tests), T011-T013 (implementation) |
| US2 | T014-T016 (tests), T017-T019 (implementation) |
| US3 | T020-T022 (tests), T023-T025 (implementation) |
| US4 | T026-T028 (tests), T029-T031 (implementation) |
| US5 | T032-T034 (tests), T035-T037 (implementation) |
| Polish | T038, T040 (independent) |

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: T008 - Unit test for TodoStore.add() in tests/test_models.py
Task: T009 - Unit test for TodoService.add_todo() in tests/test_service.py
Task: T010 - CLI integration test for add command in tests/test_cli.py

# Launch all implementation for User Story 1 together:
Task: T011 - Implement add CLI command in todo/cli.py
Task: T012 - Connect CLI add to TodoService
Task: T013 - Add input validation
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test `add` command independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP!
3. Add User Story 2 → Test independently → Full list view
4. Add User Story 3 → Test independently → Complete functionality
5. Add User Story 4 → Test independently → Update feature
6. Add User Story 5 → Test independently → Delete feature
7. Polish phase → Documentation and cleanup

### Recommended Order

**P1 Stories (parallel-safe after foundation)**:
- US1: Add (T003)
- US2: View (T004)
- US3: Complete (T005)

**P2 Stories (after P1, can parallelize)**:
- US4: Update (T006)
- US5: Delete (T007)

---

## Quick Reference

| Metric | Value |
|--------|-------|
| Total Tasks | 41 |
| Setup Tasks | 4 |
| Foundational Tasks | 3 |
| User Story Tasks | 30 |
| Polish Tasks | 4 |
| Test Tasks | 15 |
| Implementation Tasks | 26 |

| User Story | Tasks | Priority |
|------------|-------|----------|
| US1: Add | T008-T013 | P1 |
| US2: View | T014-T019 | P1 |
| US3: Complete | T020-T025 | P1 |
| US4: Update | T026-T031 | P2 |
| US5: Delete | T032-T037 | P2 |

---

## Notes

- **[P] tasks** = different files, no dependencies on incomplete tasks
- **[Story] label** maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (red phase)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
