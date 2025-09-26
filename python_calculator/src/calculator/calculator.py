"""Calculator class implementation.

This module provides a Calculator class that uses the operations module.
"""
from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.

    This class uses the functions from the operations module to perform
    calculations and keeps track of calculation history.
    """

    def __init__(self):
        """Initialize a new Calculator with empty history."""
        self.history = []

    def add(self, a, b):
        """
        Add two numbers and store the operation in history.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """
        Subtract b from a and store the operation in history.

        Args:
            a: Number to subtract from
            b: Number to subtract

        Returns:
            The difference (a - b)
        """
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """
        Multiply two numbers and store the operation in history.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """
        Divide a by b and store the operation in history.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            The quotient a/b

        Raises:
            ZeroDivisionError: If b is 0
        """
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """
        Return the calculation history.

        Returns:
            A list of strings representing the calculation history
        """
        return self.history
