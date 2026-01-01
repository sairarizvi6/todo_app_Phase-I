"""Unit tests for the todo service layer."""

import pytest

from src.models import Todo, TodoStore
from src.service import (
    TodoAlreadyCompleteError,
    TodoNotFoundError,
    TodoService,
)


class TestTodoService:
    """Tests for the TodoService class."""

    def test_add_todo(self) -> None:
        """Test adding a todo through the service."""
        service = TodoService()
        todo = service.add_todo("Buy groceries")

        assert todo.id == 1
        assert todo.text == "Buy groceries"
        assert todo.completed is False

    def test_add_todo_empty_text_raises_error(self) -> None:
        """Test that adding an empty todo raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Todo text cannot be empty"):
            service.add_todo("")

    def test_add_todo_whitespace_only_raises_error(self) -> None:
        """Test that adding whitespace-only text raises ValueError."""
        service = TodoService()

        with pytest.raises(ValueError, match="Todo text cannot be empty"):
            service.add_todo("   ")

    def test_add_todo_strips_whitespace(self) -> None:
        """Test that whitespace is stripped from todo text."""
        service = TodoService()
        todo = service.add_todo("  Buy groceries  ")

        assert todo.text == "Buy groceries"

    def test_get_todos(self) -> None:
        """Test retrieving all todos."""
        service = TodoService()
        service.add_todo("Todo 1")
        service.add_todo("Todo 2")

        todos = service.get_todos()
        assert len(todos) == 2

    def test_get_todos_empty(self) -> None:
        """Test retrieving todos when none exist."""
        service = TodoService()
        todos = service.get_todos()
        assert todos == []

    def test_complete_todo(self) -> None:
        """Test completing a todo."""
        service = TodoService()
        service.add_todo("Buy groceries")

        todo = service.complete_todo(1)

        assert todo.completed is True

    def test_complete_todo_not_found(self) -> None:
        """Test completing a non-existent todo."""
        service = TodoService()

        with pytest.raises(TodoNotFoundError):
            service.complete_todo(999)

    def test_complete_already_complete_raises_error(self) -> None:
        """Test that completing an already-complete todo raises error."""
        service = TodoService()
        service.add_todo("Buy groceries")
        service.complete_todo(1)

        with pytest.raises(TodoAlreadyCompleteError):
            service.complete_todo(1)

    def test_update_todo(self) -> None:
        """Test updating a todo's text."""
        service = TodoService()
        service.add_todo("Buy grocieres")

        todo = service.update_todo(1, "Buy groceries")

        assert todo.text == "Buy groceries"

    def test_update_todo_not_found(self) -> None:
        """Test updating a non-existent todo."""
        service = TodoService()

        with pytest.raises(TodoNotFoundError):
            service.update_todo(999, "New text")

    def test_update_todo_empty_text_raises_error(self) -> None:
        """Test that updating with empty text raises ValueError."""
        service = TodoService()
        service.add_todo("Buy groceries")

        with pytest.raises(ValueError, match="Todo text cannot be empty"):
            service.update_todo(1, "")

    def test_delete_todo(self) -> None:
        """Test deleting a todo."""
        service = TodoService()
        service.add_todo("Buy groceries")

        result = service.delete_todo(1)

        assert result is True
        assert service.get_todos() == []

    def test_delete_todo_not_found(self) -> None:
        """Test deleting a non-existent todo."""
        service = TodoService()

        with pytest.raises(TodoNotFoundError):
            service.delete_todo(999)

    def test_sequential_ids(self) -> None:
        """Test that IDs are assigned sequentially."""
        service = TodoService()
        todo1 = service.add_todo("Todo 1")
        todo2 = service.add_todo("Todo 2")
        todo3 = service.add_todo("Todo 3")

        assert todo1.id == 1
        assert todo2.id == 2
        assert todo3.id == 3

    def test_service_uses_provided_store(self) -> None:
        """Test that service uses a provided store."""
        store = TodoStore()
        service = TodoService(store)

        assert service.store is store

    def test_service_creates_store_if_none(self) -> None:
        """Test that service creates a store if none provided."""
        service = TodoService()
        assert service.store is not None
        assert isinstance(service.store, TodoStore)
