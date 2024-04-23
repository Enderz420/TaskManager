import click


@click.group()
def cli():
    """This script showcases different terminal UI helpers in Click."""
    pass

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
            click.echo("  q: quit")
            char = click.getchar()
            if char == "a":
                menu = "add"
            elif char == "q":
                menu = "quit"
            elif char == "m":
                menu = "modify"
            elif char == "d":
                menu = "d"
            else:
                click.echo("Invalid input")
        elif menu == "add":
            click.echo("  a: add task")
            click.echo("  b: back")
            char = click.getchar()
            if char == "b":
                menu = "main"
            else:
                click.echo("Invalid input")
        elif menu == "modify":
            click.echo("  which task do you want to modify?")
        elif menu == "quit":
            return

if __name__ == "__main__":
    menu()