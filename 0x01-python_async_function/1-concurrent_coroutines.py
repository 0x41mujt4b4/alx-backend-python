#!/usr/bin/env python3
"""Asynch function that waits for random delay and returns it"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """Asynch function that waits for random delay and returns it"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in delays]