# Todo - In-Memory Python Console App

A simple command-line todo application built with Python 3.13+. This is Phase I of the AI-Native Todo Platform.

## Features

- **Add todos**: `todo add "Buy groceries"`
- **List todos**: `todo list`
- **Complete todos**: `todo complete 1`
- **Update todos**: `todo update 1 "New description"`
- **Delete todos**: `todo delete 1`

## Requirements

- Python 3.13+
- UV (recommended) or pip

## Installation

```bash
# Using UV (recommended)
uv pip install -e .

# Or using pip
pip install -e .
```

## Usage

```bash
# Show help
todo --help

# Add a new todo
todo add "Buy groceries"

# List all todos
todo list

# Mark a todo as complete
todo complete 1

# Update a todo's text
todo update 1 "Buy groceries and milk"

# Delete a todo
todo delete 1
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=todo --cov-report=term-missing
```

## Project Structure

```
todo/
├── __init__.py       # Package init
├── __main__.py       # Entry point for `python -m todo`
├── cli.py            # CLI commands (Click framework)
├── main.py           # Entry point
├── models.py         # Todo dataclass and TodoStore
└── service.py        # TodoService business logic
tests/
├── __init__.py
├── test_cli.py       # CLI integration tests
├── test_models.py    # Model unit tests
└── test_service.py   # Service unit tests
pyproject.toml        # Project configuration
```

## Architecture

The app follows a layered architecture:

1. **Model Layer** (`models.py`): Todo data class and in-memory storage
2. **Service Layer** (`service.py`): Business logic and error handling
3. **UI Layer** (`cli.py`): Console interface using Click

## License

MIT
"# todo_app_Phase-I" 
# todo_app_Phase-I
