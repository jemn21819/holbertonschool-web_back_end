#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n should return the list of all the delays (float values)
    """
    list_wait: List[float] = []
    for i in range(n):
        list_wait.append(await wait_random(max_delay))
    return sorted(list_wait)
