import time
from typing import Dict, List

from .compile import compile_pattern


def benchmark_pattern(
    pattern: str, text: str, iterations: int = 1000, flags: int = 0
) -> float:
    """
    Benchmark regex pattern performance.

    Args:
        pattern: Regex pattern to benchmark
        text: Text to search
        iterations: Number of iterations to run
        flags: Regex flags

    Returns:
        Average execution time in milliseconds
    """
    compiled = compile_pattern(pattern, flags)
    start_time = time.perf_counter()
    for _ in range(iterations):
        compiled.search(text)
    end_time = time.perf_counter()
    return ((end_time - start_time) / iterations) * 1000


def compare_patterns(
    patterns: List[str], text: str, iterations: int = 1000
) -> Dict[str, float]:
    """
    Compare performance of multiple patterns.

    Args:
        patterns: List of regex patterns to compare
        text: Text to search
        iterations: Number of iterations per pattern

    Returns:
        Dictionary mapping patterns to average execution time in milliseconds
    """
    results = {}
    for pattern in patterns:
        avg_time = benchmark_pattern(pattern, text, iterations)
        results[pattern] = avg_time
    return results
