import re
from typing import Callable


def replace_all(
    pattern: str, replacement: str, text: str, count: int = 0, flags: int = 0
) -> str:
    """
    Replace all occurrences of pattern.

    Args:
        pattern: Regex pattern string
        replacement: Replacement string (can include backreferences)
        text: Text to perform replacement on
        count: Maximum number of replacements (0 = unlimited)
        flags: Regex flags

    Returns:
        Text with replacements applied
    """
    return re.sub(pattern, replacement, text, count, flags)


def replace_with_function(
    pattern: str,
    repl_func: Callable[[re.Match], str],
    text: str,
    count: int = 0,
    flags: int = 0,
) -> str:
    """
    Replace matches using a callback function.

    Args:
        pattern: Regex pattern string
        repl_func: Function that takes Match object and returns replacement string
        text: Text to perform replacement on
        count: Maximum number of replacements (0 = unlimited)
        flags: Regex flags

    Returns:
        Text with replacements applied
    """
    return re.sub(pattern, repl_func, text, count, flags)


def remove_pattern(pattern: str, text: str, flags: int = 0) -> str:
    """
    Remove all occurrences of pattern from text.

    Args:
        pattern: Regex pattern string
        text: Text to clean
        flags: Regex flags

    Returns:
        Text with pattern removed
    """
    return re.sub(pattern, "", text, flags=flags)
