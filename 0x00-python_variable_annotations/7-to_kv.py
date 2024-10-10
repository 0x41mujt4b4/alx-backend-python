#!/usr/bin/env python3
"""Type annotation module of to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the key and the square of the value"""
    return (k, v ** 2)
