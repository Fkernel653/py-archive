"""Fast string operations."""

from typing import Dict, List


def join_strings(strings: List[str], sep: str = "") -> str:
    """Concatenate strings efficiently (faster than += in loops).

    Args:
        strings: List of strings to join.
        sep: String placed between elements.

    Returns:
        Concatenated string.
    """
    return sep.join(strings)


def buffer_join(builder: List[str], final_separator: str = "") -> str:
    """Join buffered strings (use for building in loops).

    Args:
        builder: List of accumulated string parts.
        final_separator: Separator between parts.

    Returns:
        Final concatenated string.
    """
    return final_separator.join(builder)


def translate_replace(text: str, replacements: Dict[str, str]) -> str:
    """Replace multiple characters quickly using translate table.

    Args:
        text: Original string.
        replacements: Dictionary of {'old': 'new'} mappings (single chars).

    Returns:
        String with replacements applied.
    """
    trans_table = str.maketrans(replacements)
    return text.translate(trans_table)


def strip_newline(line: str) -> str:
    """Remove only trailing newline (faster than strip()).

    Args:
        line: String that may end with newline.

    Returns:
        String without trailing newline.
    """
    return line.rstrip("\n")
