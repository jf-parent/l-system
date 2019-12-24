#!/usr/bin/env python

import turtle
import _tkinter
import glob
import os
import importlib

import click
from IPython import embed

from lib.l_system import render_l_system


@click.group()
def cli():
    pass


@click.command()
def list():
    for file_ in sorted(glob.glob("systems/*.py")):
        system = file_.split(os.sep)[1].replace(".py", "")
        click.echo(f"[*] {system}")


@click.command()
@click.argument('system')
@click.option('-d', '--delay', default=0, help='Sleep for x seconds before drawing <default: 0>')
@click.option('-v', '--verbose', default=False, help='Verbose <default: 0>')
def run(system, delay, verbose):
    click.echo(f"[*]Rendering {system}")
    try:
        system_module = getattr(__import__("systems", fromlist=[system]), system)
    except AttributeError:
        click.echo("System not found")
        exit(1)
    except Exception:
        raise

    os.environ["TK_SILENCE_DEPRECATION"] = "1"

    args = ['rules', 'axiom', 'iterations', 'segment_length', 'alpha_zero', 'angle']
    try:
        render_l_system(
            *[getattr(system_module, a) for a in args],
            debug=verbose,
            delay=delay
        )
    except (_tkinter.TclError, turtle.Terminator):
        print("Aborting")


cli.add_command(run)
cli.add_command(list)


if __name__ == '__main__':
    cli()
