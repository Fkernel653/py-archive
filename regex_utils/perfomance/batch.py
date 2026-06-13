import re
from typing import Dict, List, Optional, Tuple

from ..compile import compile_pattern


def batch_search(
    pattern: str, texts: List[str], flags: int = 0
) -> List[Optional[re.Match]]:
    """
    Search pattern in multiple texts efficiently.
    Pattern is compiled once and reused for all texts.

    Args:
        pattern: Regex pattern string
        texts: List of texts to search
        flags: Regex flags

    Returns:
        List of Match objects (or None for each text)
    """
    compiled = compile_pattern(pattern, flags)
    return [compiled.search(text) for text in texts]


def batch_replace(
    pattern: str, replacement: str, texts: List[str], count: int = 0, flags: int = 0
) -> List[str]:
    """
    Replace pattern in multiple texts efficiently.
    Pattern is compiled once and reused for all texts.

    Args:
        pattern: Regex pattern string
        replacement: Replacement string
        texts: List of texts to process
        count: Maximum number of replacements per text
        flags: Regex flags

    Returns:
        List of texts with replacements
    """
    compiled = compile_pattern(pattern, flags)
    return [compiled.sub(replacement, text, count) for text in texts]


def batch_filter(pattern: str, texts: List[str], flags: int = 0) -> List[str]:
    """
    Filter texts that match the pattern.
    Pattern is compiled once.

    Args:
        pattern: Regex pattern string
        texts: List of texts to filter
        flags: Regex flags

    Returns:
        List of texts that match the pattern
    """
    compiled = compile_pattern(pattern, flags)
    return [text for text in texts if compiled.search(text)]


def multi_pattern_search(
    patterns: List[str], text: str, flags: int = 0
) -> Dict[str, Optional[re.Match]]:
    """
    Search multiple patterns in a single text.
    Each pattern is compiled once.

    Args:
        patterns: List of regex pattern strings
        text: Text to search in
        flags: Regex flags

    Returns:
        Dictionary mapping patterns to their Match objects (or None)
    """
    results = {}
    for pattern in patterns:
        compiled = compile_pattern(pattern, flags)
        results[pattern] = compiled.search(text)
    return results


def first_matching_pattern(
    patterns: List[str], text: str, flags: int = 0
) -> Optional[Tuple[str, re.Match]]:
    """
    Find first pattern that matches the text.
    Useful for checking multiple possible patterns.

    Args:
        patterns: List of regex pattern strings
        text: Text to search in
        flags: Regex flags

    Returns:
        Tuple of (pattern, match) or None if no pattern matches
    """
    for pattern in patterns:
        compiled = compile_pattern(pattern, flags)
        match = compiled.search(text)
        if match:
            return (pattern, match)
    return None
