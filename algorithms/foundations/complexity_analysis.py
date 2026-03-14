"""
Complexity Analysis Utilities
==============================

Tools to measure and compare algorithm performance empirically.
Useful for demonstrating how Big O manifests in real execution times.
"""

import time
import functools
from typing import Callable, Any, Dict


def complexity(time_complexity: str, space_complexity: str):
    """
    Decorator that annotates a function with its complexity.

    Usage:
        @complexity("O(n)", "O(1)")
        def linear_search(arr, target):
            ...

    The decorated function gains a `.complexity` attribute:
        linear_search.complexity
        # {'time': 'O(n)', 'space': 'O(1)'}
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.complexity = {
            "time": time_complexity,
            "space": space_complexity,
        }
        return wrapper

    return decorator


def measure_time(func: Callable, *args, **kwargs) -> Dict[str, Any]:
    """
    Measure the execution time of a function call.

    Returns:
        {
            "result": <function return value>,
            "time_ms": <elapsed time in milliseconds>,
            "function": <function name>,
        }
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = (time.perf_counter() - start) * 1000  # Convert to ms

    return {
        "result": result,
        "time_ms": round(elapsed, 4),
        "function": func.__name__,
    }


def compare_algorithms(algorithms: list, input_generator: Callable,
                        sizes: list) -> list:
    """
    Compare multiple algorithms across different input sizes.

    Args:
        algorithms: List of functions to compare.
        input_generator: Callable that takes a size and returns input data.
                         e.g., lambda n: list(range(n))
        sizes: List of input sizes to test.
                e.g., [100, 1000, 10000]

    Returns:
        List of dicts with benchmark results for each algorithm and size.

    Example:
        results = compare_algorithms(
            [bubble_sort, merge_sort],
            lambda n: random.sample(range(n), n),
            [100, 500, 1000]
        )
    """
    results = []

    for size in sizes:
        data = input_generator(size)

        for algo in algorithms:
            # Create a copy so each algorithm gets the same input
            input_copy = list(data) if isinstance(data, list) else data
            measurement = measure_time(algo, input_copy)

            results.append({
                "algorithm": algo.__name__,
                "input_size": size,
                "time_ms": measurement["time_ms"],
                "complexity": getattr(algo, "complexity", None),
            })

    return results
