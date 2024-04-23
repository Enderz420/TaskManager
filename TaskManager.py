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
    click.echo("Task naming format should be Task(Number). No spaces should be used either.")
    click.echo("What the task is should be specified in the description as to avoid conflicts in code.")
    title = click.prompt("What is the title of the task?\n", type=str, default="Task1")

@cli.command()
def modify_task():
    click.echo("  Which task do you want to modify?")
    click.echo(tasks)
    mtask = click.getchar()

@cli.command()
def delete_task():
    click.echo("  Conducing this operation permanently deletes the task, use at own risk.")
    click.echo("  To exit at any time, close the program.")
    reqFile = click.prompt("Which file do you want to delete?", type=str,)
    if os.path.isfile(reqFile):
        os.remove(f"Tasks/{reqFile}")

@cli.command()
def menu():
    """Shows a simple menu."""
    menu = "main"
    while True:
        if menu == "main":
            click.echo("Main menu:")
            click.echo("  a: add task")
            click.echo("  m: modify existing task")
            click.echo("  d: delete task")
            click.echo("  q: quit\n")
            char = click.getchar()
            if char == "a":
                menu = "add"
            elif char == "q":
                menu = "quit"
            elif char == "m":
                menu = "modify"
            elif char == "d":
                menu = "delete"
            else:
                click.echo("Invalid input")
        elif menu == "add":
            click.echo("Add a new Task")
            click.echo("  a: add task")
            click.echo("  b: back")
            char = click.getchar()
            if char == "a":
                new_task()
            elif char == "b":
                menu = "main"
            else:
                click.echo("Invalid input")
        elif menu == "modify":
            modify_task()
        elif menu == "delete":
            click.echo("  Conducing this operation permanently deletes the task, use at own risk.")


        elif menu == "quit":
            return

if __name__ == "__main__":
    menu()