"""Business logic service for the todo application.

Provides a service layer that wraps the TodoStore with higher-level
operations and error handling.
"""

from typing import List

from src.models import Todo, TodoStore


class TodoServiceError(Exception):
    """Base exception for todo service errors."""

    pass


class TodoNotFoundError(TodoServiceError):
    """Raised when a todo item is not found."""

    def __init__(self, todo_id: int) -> None:
        """Initialize the error with the todo ID.

        Args:
            todo_id: The ID of the todo that was not found.
        """
        self.todo_id = todo_id
        super().__init__(f"Todo with ID {todo_id} not found")


class TodoAlreadyCompleteError(TodoServiceError):
    """Raised when trying to complete an already-complete todo."""

    def __init__(self, todo_id: int) -> None:
        """Initialize the error with the todo ID.

        Args:
            todo_id: The ID of the todo that is already complete.
        """
        self.todo_id = todo_id
        super().__init__(f"Todo with ID {todo_id} is already complete")


class TodoService:
    """Service layer for todo operations.

    Wraps TodoStore with business logic and error handling.
    """

    def __init__(self, store: TodoStore | None = None) -> None:
        """Initialize the service with an optional store.

        Args:
            store: The TodoStore to use. If None, creates a new one.
        """
        self._store = store if store is not None else TodoStore()

    @property
    def store(self) -> TodoStore:
        """Return the underlying store."""
        return self._store

    def add_todo(self, text: str) -> Todo:
        """Add a new todo item.

        Args:
            text: The description of the todo.

        Returns:
            The newly created Todo.

        Raises:
            ValueError: If text is empty or whitespace.
        """
        if not text or not text.strip():
            raise ValueError("Todo text cannot be empty")
        return self._store.add(text.strip())

    def get_todos(self) -> List[Todo]:
        """Retrieve all todo items.

        Returns:
            A list of all todos.
        """
        return self._store.get_all()

    def complete_todo(self, todo_id: int) -> Todo:
        """Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to complete.

        Returns:
            The updated Todo.

        Raises:
            TodoNotFoundError: If todo with given ID doesn't exist.
            TodoAlreadyCompleteError: If todo is already complete.
        """
        todo = self._store.get_by_id(todo_id)
        if todo is None:
            raise TodoNotFoundError(todo_id)
        if todo.completed:
            raise TodoAlreadyCompleteError(todo_id)
        return self._store.complete(todo_id)  # type: ignore[return-value]

    def update_todo(self, todo_id: int, text: str) -> Todo:
        """Update a todo's text.

        Args:
            todo_id: The ID of the todo to update.
            text: The new text for the todo.

        Returns:
            The updated Todo.

        Raises:
            TodoNotFoundError: If todo with given ID doesn't exist.
            ValueError: If text is empty or whitespace.
        """
        if not text or not text.strip():
            raise ValueError("Todo text cannot be empty")
        todo = self._store.get_by_id(todo_id)
        if todo is None:
            raise TodoNotFoundError(todo_id)
        return self._store.update(todo_id, text.strip())  # type: ignore[return-value]

    def delete_todo(self, todo_id: int) -> bool:
        """Delete a todo item.

        Args:
            todo_id: The ID of the todo to delete.

        Returns:
            True if deleted, False if not found.

        Raises:
            TodoNotFoundError: If todo with given ID doesn't exist.
        """
        if not self._store.get_by_id(todo_id):
            raise TodoNotFoundError(todo_id)
        return self._store.delete(todo_id)
