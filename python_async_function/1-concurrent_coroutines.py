#!/usr/bin/env python3
'''async function module'''
import asyncio
from random import triangular
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    '''async func that returns a list with the wait-times sorted low-high'''
    tasks = [wait_random(max_delay) for _ in range(n)] 
    results = []
    for future in asyncio.as_completed(tasks):
        result = await future
        results.append(result)
    return results
