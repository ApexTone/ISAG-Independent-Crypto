# https://typer.tiangolo.com/
import typer
from typing import List

from echo_utils import *
from encoding.caesar import encode_caesar
from decoding.caesar import decode_caesar

app = typer.Typer()


@app.command()
def decode(crypt_type: str, args: List[str]):
    if crypt_type == 'caesar':
        if len(args) != 2:
            echo_error('Caesar decoding need exactly 2 arguments')
            raise typer.Exit()
        if not args[1].isnumeric():
            echo_error('Second argument must be a positive integer')
            raise typer.Exit()
        echo_success(decode_caesar(args[0], int(args[1])))
    else:
        echo_success('Unsupported decoding algorithm')


@app.command()
def encode(crypt_type: str, args: List[str]):
    if crypt_type == 'caesar':
        if len(args) != 2:
            echo_error('Caesar decoding need exactly 2 arguments')
            raise typer.Exit()
        if not args[1].isnumeric():
            echo_error('Second argument must be a positive integer')
            raise typer.Exit()
        echo_success(encode_caesar(args[0], int(args[1])))
    else:
        echo_success('Unsupported encoding algorithm')


if __name__ == '__main__':
    app()
