import builtins
import sys
from rich.console import Console

console = Console()

_original_print = builtins.print  # backup (boa prática)

def rich_print(*args, sep=" ", end="\n", file=None, flush=False):
    # Se alguém pedir stderr, respeite
    if file is sys.stderr:
        console.print(*args, sep=sep, end=end, style="bold red")
    else:
        console.print(*args, sep=sep, end=end)

    if flush:
        sys.stdout.flush()

builtins.print = rich_print
