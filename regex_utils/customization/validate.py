import re


def is_match(pattern: str, text: str, flags: int = 0) -> bool:
    """
    Check if text matches pattern from the start.

    Args:
        pattern: Regex pattern string
        text: Text to validate
        flags: Regex flags

    Returns:
        True if pattern matches from start of text
    """
    return bool(re.match(pattern, text, flags))


def contains_pattern(pattern: str, text: str, flags: int = 0) -> bool:
    """
    Check if text contains the pattern anywhere.

    Args:
        pattern: Regex pattern string
        text: Text to check
        flags: Regex flags

    Returns:
        True if pattern found anywhere in text
    """
    return bool(re.search(pattern, text, flags))


def is_full_match(pattern: str, text: str, flags: int = 0) -> bool:
    """
    Check if entire text matches the pattern completely.

    Args:
        pattern: Regex pattern string
        text: Text to validate
        flags: Regex flags

    Returns:
        True if entire string matches pattern
    """
    return bool(re.fullmatch(pattern, text, flags))


def count_matches(pattern: str, text: str, flags: int = 0) -> int:
    """
    Count number of non-overlapping matches.

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        Number of matches found
    """
    return len(re.findall(pattern, text, flags))
