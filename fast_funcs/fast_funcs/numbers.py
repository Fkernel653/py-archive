"""Fast numeric operations."""

import math


def sum_precise(float_list: list[float]) -> float:
    """Sum floats with error compensation (more accurate than sum()).

    Args:
        float_list: List of floating point numbers.

    Returns:
        Precise sum with compensated rounding errors.
    """
    return math.fsum(float_list)


def square(x: float) -> int | float:
    """Fast square using multiplication (faster than pow(x, 2)).

    Args:
        x: Number to square.

    Returns:
        x squared.
    """
    return x * x


def fast_round(x: float, decimals: int = 0) -> int | float:
    """Round using integer operations (faster than round()).

    Args:
        x: Number to round.
        decimals: Number of decimal places (default: 0).

    Returns:
        Rounded number.
    """
    factor = 10**decimals
    result = int(x * factor + (0.5 if x >= 0 else -0.5)) / factor
    return int(result) if decimals == 0 else result
