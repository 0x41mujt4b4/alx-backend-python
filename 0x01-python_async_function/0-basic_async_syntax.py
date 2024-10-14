#!/usr/bin/env python3
"""Basic async syntax"""
from random import randint
import asyncio


async def wait_random(max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay"""
    delay = randint(1, max_delay)
    await asyncio.sleep(delay)
    return delay