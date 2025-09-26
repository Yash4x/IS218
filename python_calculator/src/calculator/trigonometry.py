"""Trigonometric functions for the calculator."""
import math

def sin(x):
    """
    Calculate the sine of x (in radians).
    
    Args:
        x: Angle in radians
        
    Returns:
        The sine of x
    """
    return math.sin(x)


def cos(x):
    """
    Calculate the cosine of x (in radians).
    
    Args:
        x: Angle in radians
        
    Returns:
        The cosine of x
    """
    return math.cos(x)

def tan(x):
    """
    Calculate the tangent of x (in radians).
    
    Args:
        x: Angle in radians
        
    Returns:
        The tangent of x
        
    Raises:
        ValueError: If x is a multiple of π/2 (undefined)
    """
    # Check for undefined values
    if abs(math.cos(x)) < 1e-10:
        raise ValueError("Tangent is undefined at this value")
    return math.tan(x)