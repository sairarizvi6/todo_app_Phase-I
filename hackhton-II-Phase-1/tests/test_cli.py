"""Integration tests for the CLI commands."""

import pytest
from click.testing import CliRunner

from src.cli import create_cli
from src.service import TodoService


@pytest.fixture
def runner() -> CliRunner:
    """Create a Click test runner."""
    return CliRunner()


@pytest.fixture
def service() -> TodoService:
    """Create a fresh TodoService for each test."""
    return TodoService()


@pytest.fixture
def cli(runner: object, service: TodoService) -> object:
    """Create a CLI instance with a fresh service."""
    return create_cli(service)


class TestCLIAdd:
    """Tests for the 'add' command."""

    def test_add_single_todo(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test adding a single todo."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["add", "Buy groceries"])

        assert result.exit_code == 0
        assert "Added todo #1: Buy groceries" in result.output
        assert len(service.get_todos()) == 1

    def test_add_multiple_todos(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test adding multiple todos."""
        cli = create_cli(service)
        runner.invoke(cli, ["add", "Buy groceries"])
        runner.invoke(cli, ["add", "Clean room"])

        assert len(service.get_todos()) == 2
        todo1 = service.get_todos()[0]
        assert todo1.id == 1
        assert service.get_todos()[1].id == 2

    def test_add_empty_text_error(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test that adding empty text shows error."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["add", ""])

        assert result.exit_code == 1
        assert "Error: Todo text cannot be empty" in result.output


class TestCLIList:
    """Tests for the 'list' command."""

    def test_list_empty(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test listing when no todos exist."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["list"])

        assert result.exit_code == 0
        assert "No todos yet" in result.output

    def test_list_with_todos(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test listing todos."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")
        service.add_todo("Clean room")

        result = runner.invoke(cli, ["list"])

        assert result.exit_code == 0
        assert "Your todos" in result.output
        assert "[ ] #1: Buy groceries" in result.output
        assert "[ ] #2: Clean room" in result.output

    def test_list_shows_completed_status(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test that list shows completed status."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")
        service.complete_todo(1)

        result = runner.invoke(cli, ["list"])

        assert result.exit_code == 0
        assert "[x] #1: Buy groceries" in result.output


class TestCLIComplete:
    """Tests for the 'complete' command."""

    def test_complete_todo(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test completing a todo."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")

        result = runner.invoke(cli, ["complete", "1"])

        assert result.exit_code == 0
        assert "Completed todo #1: Buy groceries" in result.output
        assert service.get_todos()[0].completed is True

    def test_complete_not_found(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test completing a non-existent todo."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["complete", "999"])

        assert result.exit_code == 1
        assert "Error: Todo #999 not found" in result.output

    def test_complete_already_complete(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test completing an already-complete todo."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")
        service.complete_todo(1)

        result = runner.invoke(cli, ["complete", "1"])

        assert result.exit_code == 1
        assert "already complete" in result.output


class TestCLIUpdate:
    """Tests for the 'update' command."""

    def test_update_todo(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test updating a todo's text."""
        cli = create_cli(service)
        service.add_todo("Buy grocieres")

        result = runner.invoke(cli, ["update", "1", "Buy groceries"])

        assert result.exit_code == 0
        assert "Updated todo #1: Buy groceries" in result.output
        assert service.get_todos()[0].text == "Buy groceries"

    def test_update_not_found(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test updating a non-existent todo."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["update", "999", "New text"])

        assert result.exit_code == 1
        assert "Error: Todo #999 not found" in result.output

    def test_update_empty_text_error(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test that updating with empty text shows error."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")

        result = runner.invoke(cli, ["update", "1", ""])

        assert result.exit_code == 1
        assert "Error: New text cannot be empty" in result.output


class TestCLIDelete:
    """Tests for the 'delete' command."""

    def test_delete_todo(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test deleting a todo."""
        cli = create_cli(service)
        service.add_todo("Buy groceries")

        result = runner.invoke(cli, ["delete", "1"])

        assert result.exit_code == 0
        assert "Deleted todo #1" in result.output
        assert len(service.get_todos()) == 0

    def test_delete_not_found(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test deleting a non-existent todo."""
        cli = create_cli(service)
        result = runner.invoke(cli, ["delete", "999"])

        assert result.exit_code == 1
        assert "Error: Todo #999 not found" in result.output

    def test_delete_preserves_remaining(
        self, runner: CliRunner, service: TodoService
    ) -> None:
        """Test that deleting one todo preserves others."""
        cli = create_cli(service)
        service.add_todo("Todo 1")
        service.add_todo("Todo 2")

        runner.invoke(cli, ["delete", "1"])

        assert len(service.get_todos()) == 1
        remaining = service.get_todos()[0]
        assert remaining.id == 2
        assert remaining.text == "Todo 2"


class TestCLIHelp:
    """Tests for CLI help and main command."""

    def test_main_help(self, runner: CliRunner) -> None:
        """Test that main help shows available commands."""
        cli = create_cli()
        result = runner.invoke(cli, ["--help"])

        assert result.exit_code == 0
        assert "add" in result.output
        assert "list" in result.output
        assert "complete" in result.output
        assert "update" in result.output
        assert "delete" in result.output
