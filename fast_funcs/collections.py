"""Fast collection operations."""

from typing import Any, Callable, Iterable, List, Optional, TypeVar, cast

T = TypeVar("T")
U = TypeVar("U")


def filter_fast(items: Iterable[T], predicate: Callable[[Any], bool]) -> List[T]:
    """Filter items using list comprehension (faster than built-in filter).

    Args:
        items: Iterable to filter.
        predicate: Function that returns True for kept items.

    Returns:
        List of items satisfying the predicate.
    """
    return [item for item in items if predicate(item)]


def map_fast(items: Iterable[T], transformer: Callable[[T], U]) -> List[U]:
    """Transform items using list comprehension (faster than built-in map).

    Args:
        items: Iterable to transform.
        transformer: Function to apply to each item.

    Returns:
        List of transformed items.
    """
    return [transformer(item) for item in items]


def reverse_copy(sequence) -> List:
    """Create reversed copy (faster than reversed() for lists).

    Args:
        sequence: Sequence to reverse (list, tuple, str).

    Returns:
        Reversed list.
    """
    return sequence[::-1]


def sort_inplace(
    items: List[T], key: Optional[Callable[[T], Any]] = None, reverse: bool = False
) -> List[T]:
    """Sort list in-place without creating a copy.

    Args:
        items: List to sort (modified in-place).
        key: Sort key function (optional).
        reverse: Sort in reverse order.

    Returns:
        The sorted list (same instance).
    """
    items.sort(key=cast(Any, key), reverse=reverse)
    return items


def flatten(nested: List[List[T]]) -> List[T]:
    """Flatten a nested list by one level (fast comprehension).

    Args:
        nested: List of lists.

    Returns:
        Flattened list.
    """
    return [item for sublist in nested for item in sublist]
