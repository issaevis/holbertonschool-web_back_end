#!/usr/bin/env python3
'''async module'''

import asyncio
import typing
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''returns the elapsed time for async_comprehension
    to run 4 times in parallel'''
    s_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    e_time = time.time()
    elapsed_time = e_time - s_time

    return elapsed_time
