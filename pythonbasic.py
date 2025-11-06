"""Sample Python code demonstrating basic concepts."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}!"


def factorial(n: int) -> int:
    """Compute factorial using a simple iterative approach."""
    if n < 0:
        raise ValueError("factorial is undefined for negative values")

    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def fibonacci(limit: int) -> list[int]:
    """Generate Fibonacci numbers up to a given count."""
    if limit < 0:
        raise ValueError("limit must be non-negative")

    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(limit):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    friends = ["Alice", "Bob", "Charlie"]
    for person in friends:
        print(greet(person))

    number = 5
    print(f"Factorial of {number}: {factorial(number)}")

    count = 10
    print(f"First {count} Fibonacci numbers: {fibonacci(count)}")
