"""Fast search and membership operations."""

from typing import Any, Callable, Dict, Iterable, Set


def build_index_map(sequence: Iterable) -> Dict[Any, int]:
    """Build dictionary mapping values to their indices for O(1) lookup.

    Args:
        sequence: Sequence of hashable values.

    Returns:
        Dictionary {value: index}.
    """
    return {value: idx for idx, value in enumerate(sequence)}


def to_set(items: Iterable) -> Set:
    """Convert iterable to set for O(1) membership testing.

    Args:
        items: Iterable to convert.

    Returns:
        Set of unique items.
    """
    return set(items)


def any_early(items: Iterable, condition: Callable[[Any], bool]) -> bool:
    """Check condition with early exit (more control than any()).

    Args:
        items: Iterable to check.
        condition: Function returning bool.

    Returns:
        True if any item satisfies condition.
    """
    for item in items:
        if condition(item):
            return True
    return False
