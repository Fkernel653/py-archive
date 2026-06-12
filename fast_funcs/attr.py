"""Fast attribute operations - bypassing MRO for better performance."""

from typing import Any, TypeVar

T = TypeVar("T")


def get_direct(obj: Any, attr_name: str, default: Any = None) -> Any:
    """Get attribute directly from __dict__ (faster than getattr).

    Args:
        obj: Object to get attribute from.
        attr_name: Name of attribute.
        default: Default value if attribute missing.

    Returns:
        Attribute value or default.

    Example:
        >>> class Point: pass
        >>> p = Point()
        >>> p.x = 10
        >>> get_direct(p, "x")
        10
        >>> get_direct(p, "y", 0)
        0
    """
    return obj.__dict__.get(attr_name, default)


def has_direct(obj: Any, attr_name: str) -> bool:
    """Check if attribute exists in __dict__ (faster than hasattr).

    Args:
        obj: Object to check.
        attr_name: Name of attribute.

    Returns:
        True if attribute exists in object's __dict__.

    Example:
        >>> class Point: pass
        >>> p = Point()
        >>> p.x = 10
        >>> has_direct(p, "x")
        True
        >>> has_direct(p, "y")
        False
    """
    return attr_name in obj.__dict__


def set_direct(obj: Any, attr_name: str, value: Any) -> None:
    """Set attribute directly in __dict__ (faster than setattr).

    Args:
        obj: Object to modify.
        attr_name: Name of attribute.
        value: Value to set.

    Example:
        >>> class Point: pass
        >>> p = Point()
        >>> set_direct(p, "x", 10)
        >>> p.x
        10
    """
    obj.__dict__[attr_name] = value


def del_direct(obj: Any, attr_name: str) -> None:
    """Delete attribute directly from __dict__.

    Args:
        obj: Object to modify.
        attr_name: Name of attribute to delete.

    Raises:
        KeyError: If attribute doesn't exist in __dict__.

    Example:
        >>> class Point: pass
        >>> p = Point()
        >>> p.x = 10
        >>> del_direct(p, "x")
        >>> hasattr(p, "x")
        False
    """
    del obj.__dict__[attr_name]


def repr_attrs(obj: Any, *attr_names: str) -> str:
    """Create string representation showing only specified attributes.

    Args:
        obj: Object to represent.
        *attr_names: Attributes to include in repr.

    Returns:
        String representation.

    Example:
        >>> class Point: pass
        >>> p = Point()
        >>> p.x, p.y = 10, 20
        >>> repr_attrs(p, "x", "y")
        'Point(x=10, y=20)'
    """
    cls_name = obj.__class__.__name__
    if not attr_names:
        attr_names = tuple(obj.__dict__.keys())
    attrs = ", ".join(f"{name}={obj.__dict__.get(name)!r}" for name in attr_names)
    return f"{cls_name}({attrs})"
