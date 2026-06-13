import re
from typing import List, Optional, Tuple


def extract_groups(
    pattern: str, text: str, flags: int = 0
) -> Optional[Tuple[str, ...]]:
    """
    Extract named or numbered groups from first match.

    Args:
        pattern: Regex pattern string with groups
        text: Text to extract from
        flags: Regex flags

    Returns:
        Tuple of group values or None if no match
    """
    match = re.search(pattern, text, flags)
    return match.groups() if match else None


def extract_dict(pattern: str, text: str, flags: int = 0) -> Optional[dict]:
    """
    Extract named groups as dictionary from first match.

    Args:
        pattern: Regex pattern string with named groups (?P<name>...)
        text: Text to extract from
        flags: Regex flags

    Returns:
        Dictionary of group names to values, or None if no match
    """
    match = re.search(pattern, text, flags)
    return match.groupdict() if match else None


def extract_all_groups(
    pattern: str, text: str, flags: int = 0
) -> List[Tuple[str, ...]]:
    """
    Extract groups from all matches.

    Args:
        pattern: Regex pattern string with groups
        text: Text to extract from
        flags: Regex flags

    Returns:
        List of tuples containing group values
    """
    matches = re.finditer(pattern, text, flags)
    return [m.groups() for m in matches]


def extract_between(
    start_pattern: str,
    end_pattern: str,
    text: str,
    include_delimiters: bool = False,
    flags: int = 0,
) -> List[str]:
    """
    Extract substrings between start and end patterns.

    Args:
        start_pattern: Starting pattern
        end_pattern: Ending pattern
        text: Text to extract from
        include_delimiters: Whether to include start and end patterns in result
        flags: Regex flags

    Returns:
        List of substrings between patterns
    """
    if include_delimiters:
        pattern = f"({start_pattern}.*?{end_pattern})"
    else:
        pattern = f"{start_pattern}(.*?){end_pattern}"
    return re.findall(pattern, text, flags)
