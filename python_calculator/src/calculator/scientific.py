"""Scientific calculator operations."""
import math

def square_root(x):
    """
    Calculate the square root of x.
    
    Args:
        x: The number to calculate the square root of
        
    Returns:
        The square root of x
        
    Raises:
        ValueError: If x is negative
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base^exponent
    """
    return math.pow(base, exponent)