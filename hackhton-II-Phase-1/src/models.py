"""Data models for the todo application."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Todo:
    """Represents a single todo item.

    Attributes:
        id: Unique identifier for the todo item.
        text: Description of the task.
        completed: Whether the task has been completed.
    """

    id: int
    text: str
    completed: bool = False


class TodoStore:
    """In-memory storage for todo items.

    Provides CRUD operations for managing todos in a simple list.
    """

    def __init__(self) -> None:
        """Initialize an empty todo store."""
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def add(self, text: str) -> Todo:
        """Add a new todo item.

        Args:
            text: The description of the todo item.

        Returns:
            The newly created Todo instance.
        """
        todo = Todo(id=self._next_id, text=text, completed=False)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all(self) -> List[Todo]:
        """Retrieve all todo items.

        Returns:
            A list of all todo items in the store.
        """
        return list(self._todos)

    def get_by_id(self, todo_id: int) -> Todo | None:
        """Retrieve a todo item by its ID.

        Args:
            todo_id: The unique identifier of the todo.

        Returns:
            The Todo instance if found, None otherwise.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def complete(self, todo_id: int) -> Todo | None:
        """Mark a todo item as complete.

        Args:
            todo_id: The unique identifier of the todo.

        Returns:
            The updated Todo instance if found, None otherwise.
        """
        todo = self.get_by_id(todo_id)
        if todo is not None:
            todo.completed = True
        return todo

    def update(self, todo_id: int, text: str) -> Todo | None:
        """Update the text of a todo item.

        Args:
            todo_id: The unique identifier of the todo.
            text: The new description for the todo.

        Returns:
            The updated Todo instance if found, None otherwise.
        """
        todo = self.get_by_id(todo_id)
        if todo is not None:
            todo.text = text
        return todo

    def delete(self, todo_id: int) -> bool:
        """Delete a todo item by its ID.

        Args:
            todo_id: The unique identifier of the todo.

        Returns:
            True if the todo was deleted, False if not found.
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                del self._todos[i]
                return True
        return False

    def count(self) -> int:
        """Return the number of todo items in the store.

        Returns:
            The total count of todo items.
        """
        return len(self._todos)
