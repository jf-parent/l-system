#!/usr/bin/env python

import turtle
import _tkinter
import glob
import os
import importlib

import click
from IPython import embed

from lib.l_system import LSystem, HOOKS
from lib import logger


@click.group()
def cli():
    pass


@click.command()
def list():
    excluded = ["__init__"]
    for file_ in sorted(glob.glob("systems/*.py")):
        system = file_.split(os.sep)[1].replace(".py", "")
        if system not in excluded:
            click.echo(f"[*] {system}")


@click.command()
@click.argument('system')
@click.option('-d', '--delay', default=0, help='Sleep for x seconds before drawing <default: 0>')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Verbose <default: False>')
def run(system, delay, verbose):
    logger.info(f"[*]Rendering {system}")

    _system = system.split(os.sep)[-1].replace('.py', '')
    try:
        system_module = getattr(__import__("systems", fromlist=[_system]), _system)
    except AttributeError:
        logger.error("System not found")
        exit(1)
    except Exception:
        raise

    os.environ["TK_SILENCE_DEPRECATION"] = "1"

    title = _system.replace('_', ' ').title()

    args = ['rules', 'axiom', 'iterations', 'segment_length', 'alpha_zero', 'angle']
    kwargs = ['length_factor']
    try:
        l_system = LSystem(
            *[getattr(system_module, a) for a in args],
            title,
            debug=verbose,
            delay=delay,
            **{k:getattr(system_module, k, None) for k in kwargs},
        )

        for hook in HOOKS:
            if hasattr(system_module, hook):
                l_system.register_hook(hook, getattr(system_module, hook))

        l_system.render()
    except (_tkinter.TclError, turtle.Terminator):
        logger.info("Aborting")


cli.add_command(run)
cli.add_command(list)


if __name__ == '__main__':
    cli()
