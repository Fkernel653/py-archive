"""Fast I/O operations."""

import sys
from typing import Optional, TextIO


def echo(
    *args,
    file: TextIO = sys.stdout,
    flush: bool = False,
    sep: str = " ",
    end: str = "\n",
) -> None:
    """Print message to file with optional buffering control.

    Args:
        *args: Values to print.
        file: File to write to (default: stdout).
        flush: Whether to flush the buffer (default: False).
        sep: Separator between arguments (default: space).
        end: String appended after last argument (default: newline).

    Example:
        >>> echo("Hello", "World", sep=" - ")
        Hello - World
    """
    file.write(sep.join([str(arg) for arg in args]) + end)
    if flush:
        file.flush()


def fast_input(prompt: Optional[str] = None) -> str:
    """Read a line from stdin with optional prompt (faster than built-in input).

    Args:
        prompt: Optional text to display before reading input.

    Returns:
        String without trailing newline character.

    Example:
        >>> name = fast_input("Enter your name: ")
        Enter your name: Alice
        >>> name
        'Alice'

    Note:
        Unlike built-in input(), this doesn't add a space after the prompt.
        Add it manually if needed: fast_input("Name: ")
    """
    if prompt is not None:
        sys.stdout.write(prompt)
        sys.stdout.flush()
    return sys.stdin.readline().rstrip("\n")
