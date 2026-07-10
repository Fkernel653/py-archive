"""Fast type checking operations."""

from typing import Any, Tuple, Type


def is_exact_type(obj: Any, target_type: Type) -> bool:
    """Check exact type (ignores inheritance, faster than isinstance).

    Args:
        obj: Object to check.
        target_type: Type to compare against.

    Returns:
        True if type matches exactly.
    """
    return type(obj) is target_type


def is_one_of(obj: Any, types: Tuple[Type, ...]) -> bool:
    """Check if object's exact type is in tuple (fast membership).

    Args:
        obj: Object to check.
        types: Tuple of types to check against.

    Returns:
        True if exact type matches any in tuple.
    """
    return type(obj) in types
