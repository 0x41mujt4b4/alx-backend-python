#!/usr/bin/env python3
"""async function that wait for task wait n"""
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    """async function that wait for task wait n"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in delays]
