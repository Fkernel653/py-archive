import re
from functools import lru_cache
from typing import Pattern


@lru_cache(maxsize=128)
def compile_pattern(pattern: str, flags: int = 0) -> Pattern:
    """
    Compile regex pattern with LRU caching for performance.
    Caches up to 128 patterns to avoid repeated compilation.

    Args:
        pattern: Regex pattern string
        flags: Regex flags (e.g., re.IGNORECASE, re.MULTILINE)

    Returns:
        Compiled regex pattern object
    """
    return re.compile(pattern, flags)


def validate_regex(pattern: str) -> bool:
    """
    Check if regex pattern is valid.

    Args:
        pattern: Regex pattern string to validate

    Returns:
        True if pattern is valid regex
    """
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


def get_pattern_info(pattern: str, flags: int = 0) -> dict:
    """
    Get information about compiled pattern.

    Args:
        pattern: Regex pattern string
        flags: Regex flags

    Returns:
        Dictionary with pattern info (groups, groupindex, flags)
    """
    compiled = compile_pattern(pattern, flags)
    return {
        "pattern": compiled.pattern,
        "groups": compiled.groups,
        "groupindex": compiled.groupindex,
        "flags": compiled.flags,
    }


def escape_regex(text: str) -> str:
    """
    Escape special characters in string for use in regex.

    Args:
        text: String to escape

    Returns:
        Escaped string safe for regex
    """
    return re.escape(text)
