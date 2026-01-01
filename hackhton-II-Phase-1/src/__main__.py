"""Entry point for running the todo package with `python -m todo`."""

from src.cli import cli


def main() -> None:
    """Main entry point for the todo CLI application."""
    cli()


if __name__ == "__main__":
    main()
