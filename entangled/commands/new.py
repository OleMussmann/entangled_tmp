from typing import Optional

import argh  # type: ignore
import logging

from rich.console import Console
from rich.table import Table

from ..config import templates


@argh.arg(
    "-l",
    "--list-templates",
    default=False,
    help="list all official templates and exit",
)
@argh.arg(
    "-t",
    "--template",
    default="mkdocs",
    choices=[t.handle for t in templates.templates],
    help="initialize a new project from this template",
)
def new(**kwargs):
    """Create a new entangled project from a template"""
    if kwargs["list_templates"]:
        table = Table(title="Official Templates")
        table.add_column("Handle")
        table.add_column("Name")
        table.add_column("URL")
        table.add_column("Description")
        for t in templates.templates:
            table.add_row(t.handle, t.name, t.url, t.description)

        console = Console()
        console.print(table)
        print()
        print("Usage: entangled new <handle>")
        print()

        return

    print(template)
