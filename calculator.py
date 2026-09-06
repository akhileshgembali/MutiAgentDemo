#!/usr/bin/env python3
"""
A small command-line calculator.

Supports: + - * / // % ** (add, subtract, multiply, divide,
floor divide, modulo, power)

Usage:
    Run the script and follow the prompts, e.g.:
        Enter first number: 10
        Enter operator (+ - * / // % **): /
        Enter second number: 4
        10 / 4 = 2.5

    Type 'q' at any prompt to quit.
"""

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
    "%": lambda a, b: a % b,
    "**": lambda a, b: a ** b,
}


def get_number(prompt):
    """Prompt until the user enters a valid number, or 'q' to quit."""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "q":
            return None
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a valid number (or 'q' to quit).")


def get_operator(prompt):
    """Prompt until the user enters a valid operator, or 'q' to quit."""
    while True:
        raw = input(prompt).strip()
        if raw.lower() == "q":
            return None
        if raw in OPERATORS:
            return raw
        print(f"  Please enter one of {', '.join(OPERATORS)} (or 'q' to quit).")


def calculate(a, op, b):
    """Apply the operator to a and b, raising ZeroDivisionError as needed."""
    return OPERATORS[op](a, b)


def format_result(value):
    """Show whole numbers without a trailing '.0'."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main():
    print("=== Simple Calculator ===")
    print(f"Operators: {', '.join(OPERATORS)}   (enter 'q' any time to quit)\n")

    while True:
        a = get_number("Enter first number: ")
        if a is None:
            break

        op = get_operator("Enter operator (+ - * / // % **): ")
        if op is None:
            break

        b = get_number("Enter second number: ")
        if b is None:
            break

        try:
            result = calculate(a, op, b)
        except ZeroDivisionError:
            print("  Error: division by zero.\n")
            continue

        print(f"{format_result(a)} {op} {format_result(b)} = {format_result(result)}\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
