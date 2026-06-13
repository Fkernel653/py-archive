import re
from typing import List, Optional, Tuple


def find_all_matches(pattern: str, text: str, flags: int = 0) -> List[str]:
    """
    Find all regex matches in text.

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        List of matched strings
    """
    return re.findall(pattern, text, flags)


def find_all_with_positions(
    pattern: str, text: str, flags: int = 0
) -> List[Tuple[int, int, str]]:
    """
    Find all matches with their positions (start, end, text).

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        List of tuples (start_position, end_position, matched_text)
    """
    return [(m.start(), m.end(), m.group()) for m in re.finditer(pattern, text, flags)]


def find_first(pattern: str, text: str, flags: int = 0) -> Optional[str]:
    """
    Find first match or return None.

    Args:
        pattern: Regex pattern string
        text: Text to search in
        flags: Regex flags

    Returns:
        First matched string or None
    """
    match = re.search(pattern, text, flags)
    return match.group() if match else None


def find_nth(pattern: str, text: str, n: int, flags: int = 0) -> Optional[str]:
    """
    Find the nth match (1-based index).

    Args:
        pattern: Regex pattern string
        text: Text to search in
        n: Match number (1-based)
        flags: Regex flags

    Returns:
        Nth matched string or None if not found
    """
    matches = re.findall(pattern, text, flags)
    return matches[n - 1] if 0 < n <= len(matches) else None
