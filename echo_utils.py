import typer


def echo_success(line):
    message = typer.style(line, fg=typer.colors.GREEN)
    typer.echo(message)


def echo_error(line):
    message = typer.style(line, fg=typer.colors.RED)
    typer.echo(message)
