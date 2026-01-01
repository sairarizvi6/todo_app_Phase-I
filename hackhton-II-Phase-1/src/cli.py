"""Command-line interface for the todo application.

Uses Click for CLI framework.
"""

import sys

import click

from src.service import (
    TodoAlreadyCompleteError,
    TodoNotFoundError,
    TodoService,
)


class TodoCLI:
    """CLI wrapper for the todo application."""

    def __init__(self, service: TodoService | None = None) -> None:
        """Initialize the CLI with an optional service.

        Args:
            service: The TodoService to use. If None, creates a new one.
        """
        self._service = service if service is not None else TodoService()

    @property
    def service(self) -> TodoService:
        """Return the underlying service."""
        return self._service


def create_cli(service: TodoService | None = None) -> click.Group:
    """Create the Click CLI group.

    Args:
        service: Optional TodoService instance to use.

    Returns:
        A Click group with all commands attached.
    """
    # Store service reference on the CLI object for tests
    _service = service if service is not None else TodoService()

    @click.group()
    @click.pass_context
    def main(ctx: click.Context) -> None:
        """Simple CLI for managing todo items."""
        # Attach service to context for commands to access
        ctx.obj = _service

    @main.command()
    @click.argument("text", nargs=-1, type=str)
    @click.pass_obj
    def add(service: TodoService, text: tuple[str, ...]) -> None:
        """Add a new todo item.

        TEXT: The description of the todo item.
        """
        todo_text = " ".join(text).strip()
        if not todo_text:
            click.echo("Error: Todo text cannot be empty.", err=True)
            click.echo("Usage: todo add <text>", err=True)
            sys.exit(1)

        try:
            todo = service.add_todo(todo_text)
            click.echo(f"Added todo #{todo.id}: {todo.text}")
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    @main.command()
    @click.pass_obj
    def list(service: TodoService) -> None:
        """List all todo items."""
        todos = service.get_todos()

        if not todos:
            click.echo("No todos yet. Add one with 'todo add <text>'")
            return

        click.echo("Your todos:")
        click.echo("-" * 40)
        for todo in todos:
            status = "[x]" if todo.completed else "[ ]"
            click.echo(f"{status} #{todo.id}: {todo.text}")
        click.echo("-" * 40)
        click.echo(f"Total: {len(todos)} todos")

    @main.command()
    @click.argument("todo_id", type=int)
    @click.pass_obj
    def complete(service: TodoService, todo_id: int) -> None:
        """Mark a todo as complete.

        TODO_ID: The ID of the todo to mark complete.
        """
        try:
            todo = service.complete_todo(todo_id)
            click.echo(f"Completed todo #{todo.id}: {todo.text}")
        except TodoNotFoundError:
            click.echo(f"Error: Todo #{todo_id} not found.", err=True)
            available_ids = [t.id for t in service.get_todos()]
            if available_ids:
                click.echo(f"Available IDs: {sorted(available_ids)}", err=True)
            sys.exit(1)
        except TodoAlreadyCompleteError:
            click.echo(f"Error: Todo #{todo_id} is already complete.", err=True)
            sys.exit(1)

    @main.command()
    @click.argument("todo_id", type=int)
    @click.argument("text", nargs=-1, type=str)
    @click.pass_obj
    def update(service: TodoService, todo_id: int, text: tuple[str, ...]) -> None:
        """Update a todo's text.

        TODO_ID: The ID of the todo to update.
        TEXT: The new description for the todo.
        """
        new_text = " ".join(text).strip()
        if not new_text:
            click.echo("Error: New text cannot be empty.", err=True)
            click.echo("Usage: todo update <todo_id> <new_text>", err=True)
            sys.exit(1)

        try:
            todo = service.update_todo(todo_id, new_text)
            click.echo(f"Updated todo #{todo.id}: {todo.text}")
        except TodoNotFoundError:
            click.echo(f"Error: Todo #{todo_id} not found.", err=True)
            available_ids = [t.id for t in service.get_todos()]
            if available_ids:
                click.echo(f"Available IDs: {sorted(available_ids)}", err=True)
            sys.exit(1)
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)

    @main.command()
    @click.argument("todo_id", type=int)
    @click.pass_obj
    def delete(service: TodoService, todo_id: int) -> None:
        """Delete a todo item.

        TODO_ID: The ID of the todo to delete.
        """
        try:
            deleted = service.delete_todo(todo_id)
            if deleted:
                click.echo(f"Deleted todo #{todo_id}")
            else:
                click.echo(f"Error: Todo #{todo_id} not found.", err=True)
                sys.exit(1)
        except TodoNotFoundError:
            click.echo(f"Error: Todo #{todo_id} not found.", err=True)
            available_ids = [t.id for t in service.get_todos()]
            if available_ids:
                click.echo(f"Available IDs: {sorted(available_ids)}", err=True)
            sys.exit(1)

    return main


# Create the default CLI instance
cli = create_cli()
