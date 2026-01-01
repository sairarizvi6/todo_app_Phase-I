"""Unit tests for the todo models."""

import pytest

from src.models import Todo, TodoStore


class TestTodo:
    """Tests for the Todo dataclass."""

    def test_todo_creation(self) -> None:
        """Test that a todo can be created with required fields."""
        todo = Todo(id=1, text="Buy groceries", completed=False)
        assert todo.id == 1
        assert todo.text == "Buy groceries"
        assert todo.completed is False

    def test_todo_default_completed(self) -> None:
        """Test that completed defaults to False."""
        todo = Todo(id=1, text="Buy groceries")
        assert todo.completed is False

    def test_todo_equality(self) -> None:
        """Test that todos with same fields are equal."""
        todo1 = Todo(id=1, text="Buy groceries", completed=False)
        todo2 = Todo(id=1, text="Buy groceries", completed=False)
        assert todo1 == todo2

    def test_todo_inequality_different_id(self) -> None:
        """Test that todos with different IDs are not equal."""
        todo1 = Todo(id=1, text="Buy groceries", completed=False)
        todo2 = Todo(id=2, text="Buy groceries", completed=False)
        assert todo1 != todo2


class TestTodoStore:
    """Tests for the TodoStore class."""

    def test_empty_store(self) -> None:
        """Test that a new store is empty."""
        store = TodoStore()
        assert store.count() == 0
        assert store.get_all() == []

    def test_add_todo(self) -> None:
        """Test adding a todo to the store."""
        store = TodoStore()
        todo = store.add("Buy groceries")

        assert todo.id == 1
        assert todo.text == "Buy groceries"
        assert todo.completed is False
        assert store.count() == 1

    def test_add_multiple_todos(self) -> None:
        """Test adding multiple todos."""
        store = TodoStore()
        todo1 = store.add("Buy groceries")
        todo2 = store.add("Clean room")

        assert todo1.id == 1
        assert todo2.id == 2
        assert store.count() == 2

    def test_get_all_todos(self) -> None:
        """Test retrieving all todos."""
        store = TodoStore()
        store.add("Todo 1")
        store.add("Todo 2")

        todos = store.get_all()
        assert len(todos) == 2
        assert todos[0].text == "Todo 1"
        assert todos[1].text == "Todo 2"

    def test_get_by_id_found(self) -> None:
        """Test getting a todo by ID when it exists."""
        store = TodoStore()
        store.add("Buy groceries")

        todo = store.get_by_id(1)
        assert todo is not None
        assert todo.text == "Buy groceries"

    def test_get_by_id_not_found(self) -> None:
        """Test getting a todo by ID when it doesn't exist."""
        store = TodoStore()
        todo = store.get_by_id(999)
        assert todo is None

    def test_complete_todo(self) -> None:
        """Test marking a todo as complete."""
        store = TodoStore()
        store.add("Buy groceries")

        todo = store.complete(1)
        assert todo is not None
        assert todo.completed is True

    def test_complete_todo_not_found(self) -> None:
        """Test completing a non-existent todo."""
        store = TodoStore()
        todo = store.complete(999)
        assert todo is None

    def test_update_todo(self) -> None:
        """Test updating a todo's text."""
        store = TodoStore()
        store.add("Buy grocieres")

        todo = store.update(1, "Buy groceries")
        assert todo is not None
        assert todo.text == "Buy groceries"

    def test_update_todo_not_found(self) -> None:
        """Test updating a non-existent todo."""
        store = TodoStore()
        todo = store.update(999, "New text")
        assert todo is None

    def test_delete_todo(self) -> None:
        """Test deleting a todo."""
        store = TodoStore()
        store.add("Buy groceries")

        result = store.delete(1)
        assert result is True
        assert store.count() == 0

    def test_delete_todo_not_found(self) -> None:
        """Test deleting a non-existent todo."""
        store = TodoStore()
        result = store.delete(999)
        assert result is False

    def test_delete_preserves_remaining_todos(self) -> None:
        """Test that deleting one todo preserves others."""
        store = TodoStore()
        store.add("Todo 1")
        store.add("Todo 2")
        store.add("Todo 3")

        store.delete(2)

        assert store.count() == 2
        todo1 = store.get_by_id(1)
        todo3 = store.get_by_id(3)
        assert todo1 is not None
        assert todo3 is not None
