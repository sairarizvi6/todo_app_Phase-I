"""Interactive menu-driven todo application."""

import sys

from src.cli import create_cli
from src.service import TodoService


def main() -> None:
    """Main interactive todo application."""
    service = TodoService()
    cli = create_cli(service)

    while True:
        print("\n" + "=" * 40)
        print("         TODO APP - MENU")
        print("=" * 40)
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Complete")
        print("6. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- ADD TASK ---")
            task = input("Enter task description: ").strip()
            if task:
                result = service.add_todo(task)
                print(f"Added: {result.text} (ID: {result.id})")
            else:
                print("Error: Task cannot be empty!")

        elif choice == "2":
            print("\n--- UPDATE TASK ---")
            todos = service.get_todos()
            if not todos:
                print("No tasks to update!")
                continue

            print("Current tasks:")
            for t in todos:
                status = "[x]" if t.completed else "[ ]"
                print(f"  {status} #{t.id}: {t.text}")

            try:
                task_id = int(input("\nEnter task ID to update: "))
                new_text = input("Enter new description: ").strip()
                if new_text:
                    result = service.update_todo(task_id, new_text)
                    print(f"Updated task #{result.id}: {result.text}")
                else:
                    print("Error: New description cannot be empty!")
            except ValueError:
                print("Error: Invalid ID!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            print("\n--- DELETE TASK ---")
            todos = service.get_todos()
            if not todos:
                print("No tasks to delete!")
                continue

            print("Current tasks:")
            for t in todos:
                status = "[x]" if t.completed else "[ ]"
                print(f"  {status} #{t.id}: {t.text}")

            try:
                task_id = int(input("\nEnter task ID to delete: "))
                service.delete_todo(task_id)
                print(f"Deleted task #{task_id}")
            except ValueError:
                print("Error: Invalid ID!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("\n--- VIEW TASKS ---")
            todos = service.get_todos()
            if not todos:
                print("No tasks yet. Add one!")
            else:
                print(f"Total: {len(todos)} tasks")
                print("-" * 40)
                for t in todos:
                    status = "[x]" if t.completed else "[ ]"
                    print(f"{status} #{t.id}: {t.text}")
                print("-" * 40)

        elif choice == "5":
            print("\n--- MARK COMPLETE ---")
            todos = service.get_todos()
            if not todos:
                print("No tasks to complete!")
                continue

            print("Current tasks:")
            for t in todos:
                status = "[x]" if t.completed else "[ ]"
                print(f"  {status} #{t.id}: {t.text}")

            try:
                task_id = int(input("\nEnter task ID to mark complete: "))
                result = service.complete_todo(task_id)
                print(f"Completed task #{result.id}: {result.text}")
            except ValueError:
                print("Error: Invalid ID!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            print("\nGoodbye!")
            sys.exit(0)

        else:
            print("\nInvalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()
