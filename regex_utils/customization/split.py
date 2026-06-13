import re
from typing import List


def split_by_pattern(
    pattern: str, text: str, maxsplit: int = 0, flags: int = 0
) -> List[str]:
    """
    Split text by regex pattern.

    Args:
        pattern: Regex pattern to split on
        text: Text to split
        maxsplit: Maximum number of splits (0 = unlimited)
        flags: Regex flags

    Returns:
        List of substrings
    """
    return re.split(pattern, text, maxsplit, flags)


def split_keep_delimiters(pattern: str, text: str, flags: int = 0) -> List[str]:
    """
    Split text but keep delimiters in the result.

    Args:
        pattern: Regex pattern to split on
        text: Text to split
        flags: Regex flags

    Returns:
        List of substrings with delimiters preserved
    """
    return re.split(f"({pattern})", text, flags=flags)
