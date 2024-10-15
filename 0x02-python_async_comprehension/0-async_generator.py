#!/usr/bin/env python3
"""async_generator module"""
import asyncio
from random import uniform


async def async_generator() -> asyncio.Generator[float]:
    """async_generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)