import typer

app = typer.Typer()


@app.command()
def hello(name: str, iq: int, display_iq: bool = True):  # display_iq has default value of true, don't need to pass to cmd
    print(f'Hello {name}')
    if display_iq:
        print(f'IQ is {iq}')


@app.command()
def goodbye():
    print('Goodbye')


if __name__ == '__main__':
    app()
