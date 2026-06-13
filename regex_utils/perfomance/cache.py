import re
from typing import List, Optional

from .compile import compile_pattern


def cached_search(pattern: str, text: str, flags: int = 0) -> Optional[re.Match]:
    """
    Perform cached regex search.
    Pattern is compiled once and cached for subsequent calls.

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        Match object or None
    """
    compiled = compile_pattern(pattern, flags)
    return compiled.search(text)


def cached_match(pattern: str, text: str, flags: int = 0) -> Optional[re.Match]:
    """
    Perform cached regex match (from start of string).
    Pattern is compiled once and cached for subsequent calls.

    Args:
        pattern: Regex pattern string
        text: Text to match
        flags: Regex flags

    Returns:
        Match object or None
    """
    compiled = compile_pattern(pattern, flags)
    return compiled.match(text)


def cached_findall(pattern: str, text: str, flags: int = 0) -> List[str]:
    """
    Find all matches using cached compiled pattern.

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        List of matched strings
    """
    compiled = compile_pattern(pattern, flags)
    return compiled.findall(text)


def cached_sub(
    pattern: str, replacement: str, text: str, count: int = 0, flags: int = 0
) -> str:
    """
    Replace using cached compiled pattern.

    Args:
        pattern: Regex pattern string
        replacement: Replacement string
        text: Text to perform replacement on
        count: Maximum number of replacements (0 = unlimited)
        flags: Regex flags

    Returns:
        Text with replacements applied
    """
    compiled = compile_pattern(pattern, flags)
    return compiled.sub(replacement, text, count)


def cached_split(
    pattern: str, text: str, maxsplit: int = 0, flags: int = 0
) -> List[str]:
    """
    Split text using cached compiled pattern.

    Args:
        pattern: Regex pattern string
        text: Text to split
        maxsplit: Maximum number of splits (0 = unlimited)
        flags: Regex flags

    Returns:
        List of substrings
    """
    compiled = compile_pattern(pattern, flags)
    return compiled.split(text, maxsplit)
