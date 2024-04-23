import click
import os
import glob

tasks = [os.path.basename(p) for p in glob.glob('Tasks/*.txt')]

@click.group()
def cli():
    """This script showcases different terminal UI helpers in Click."""
    pass

@cli.command()
def new_task():
    click.echo("  Task naming format should be Task(Number). No spaces should be used either.")
    click.echo("  What the task is should be specified in the description as to avoid conflicts in code.")
    filename = click.prompt("What would you like the filename to be? Example = 'Example.txt' \n(Keep in mind this will be used to reference the file later on if you want to modify it.)", type=str)
    title = click.prompt("What is the title of the task?\n", type=str, default="Task1")
    difficulty = click.prompt("How hard is the task?", type=str, default="None")
    description = click.prompt("Describe the task", type=str, default="This is a default description")

    location = "./Tasks"
    path = os.path.join(location, filename)
    try:
        with open(path, "x") as file:
            file.write("Title = " + repr(title) + "\n")
            file.write("Difficulty = " + repr(difficulty) + "\n")
            file.write("Description = " + repr(description) + "\n")
            return
    except FileExistsError:
        click.echo("File already exists")
        return

@cli.command()
def view_tasks():
    click.echo(tasks)
    task = click.prompt("  Which task do you want to view? Example = Task4.txt", type=str)
    location = "./Tasks"
    path = os.path.join(location, task)
    try:
        with open(path, "r") as file:
            lines = file.read()
            click.echo(lines)
    except FileNotFoundError:
        click.echo("File either doesn't exist or wasn't found. Please try again later")
@cli.command()
def delete_task():
    click.echo("  Conducing this operation permanently deletes the task, use at own risk.")
    click.echo("  To exit at any time, close the program.")
    click.echo(tasks)
    reqFile = click.prompt("  Which file do you want to delete? Format = 'Examplefile.txt'", type=str,)
    location = "./Tasks"
    path = os.path.join(location, reqFile)
    try:
        os.remove(path)
    except FileNotFoundError:
        click.echo("File not found, please try again")

@cli.command()
def menu():
    """Shows a simple menu."""
    menu = "main"
    while True:
        if menu == "main":
            click.echo("Main menu:")
            click.echo("  a: add task")
            click.echo("  v: view tasks")
            click.echo("  d: delete task")
            click.echo("  q: quit")
            char = click.getchar()
            if char == "a":
                menu = "add"
            elif char == "q":
                menu = "quit"
            elif char == "v":
                menu = "view"
            elif char == "d":
                menu = "delete"
            else:
                click.echo("Invalid input")
        elif menu == "add":
            new_task()
        elif menu == "view":
            view_tasks()
        elif menu == "delete":
            delete_task()
        elif menu == "quit":
            return

if __name__ == "__main__":
    menu()