#!/usr/bin/env python3
"""Type annotation module of make_multiplier function"""

def make_multiplier(multiplier: float) -> callable:
    """Return a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """Return the product of n and multiplier"""
        return n * multiplier
    return multiply
