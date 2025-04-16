from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import os

console = Console()

def find_file(filename, search_path):
    console.print(f"\n🔍 Searching for [bold cyan]{filename}[/bold cyan]...\n")
    with Progress(
        SpinnerColumn(style="bold magenta"),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("Searching...", total=None)
        matches = []
        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file == filename:
                    matches.append(os.path.join(root, file))
        progress.remove_task(task)
    return matches

filename = input("Enter filename to search: ")
results = find_file(filename, "/")  # use "/" or specific directory

if results:
    console.print(f"\n✅ Found {len(results)} file(s):\n", style="green")
    for path in results:
        console.print(f"[bold yellow]{path}[/bold yellow]")
else:
    console.print("\n❌ No file found.", style="red")
