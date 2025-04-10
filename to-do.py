import json
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.columns import Columns

console = Console()
TASK_FILE = "tasks.json"

# Initialize tasks as an empty list if not loaded from the file
tasks = []

# ----------------------------
# Load/Save Helpers
# ----------------------------

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# ----------------------------
# Task Functions
# ----------------------------

# Updated list_tasks function to use Align and Panel for better visuals
def list_tasks():
    if not tasks:
        console.print(Panel("[yellow]No tasks yet![/yellow]", style="bold red"))
        return

    table = Table(title=Align("📝 Your Todo List", align="center", style="bold magenta"))
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Status", style="green")

    for i, task in enumerate(tasks):
        status = "[x] Done" if task["done"] else "[ ] Not done"
        table.add_row(str(i), task["title"], status)

    console.print(Panel(table, title="[bold cyan]Tasks[/bold cyan]", border_style="blue"))

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks()
    console.print(f"[green]Task added![/green]")

def delete_task():
    list_tasks()
    try:
        idx = int(input("Enter task ID to delete: "))
        removed = tasks.pop(idx)
        save_tasks()
        console.print(f"[red]Deleted:[/red] {removed['title']}")
    except (ValueError, IndexError):
        console.print("[bold red]Invalid ID![/bold red]")

def mark_complete():
    list_tasks()
    try:
        idx = int(input("Enter task ID to toggle complete: "))
        tasks[idx]["done"] = not tasks[idx]["done"]
        save_tasks()
        console.print(f"[green]Toggled status for:[/green] {tasks[idx]['title']}")
    except (ValueError, IndexError):
        console.print("[bold red]Invalid ID![/bold red]")

# ----------------------------
# Main Loop
# ----------------------------

# Updated main menu to use Align and Panel for better visuals
def main():
    while True:
        console.print(Panel(Align("[bold cyan]Todo List Manager[/bold cyan]", align="center"), border_style="green"))
        console.print(Columns([
            Text("1. List Tasks", style="cyan"),
            Text("2. Add Task", style="magenta"),
            Text("3. Mark Task as Complete", style="green"),
            Text("4. Delete Task", style="red"),
            Text("5. Quit", style="blue")
        ]))

        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            console.print(Panel("[bold blue]Goodbye![/bold blue]", border_style="blue"))
            break
        else:
            console.print(Panel("[bold red]Invalid choice![/bold red]", border_style="red"))

# ----------------------------
# Run It!
# ----------------------------

if __name__ == "__main__":
    tasks = load_tasks()
    main()
