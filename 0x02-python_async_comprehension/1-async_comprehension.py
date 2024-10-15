#!/usr/bin/env python3
"""async_comprehension module"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generate a list of random floats using an async generator"""
    return [_ async for _ in async_generator()]
