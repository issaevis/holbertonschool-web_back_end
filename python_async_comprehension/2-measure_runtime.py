#!/usr/bin/env python3
'''async module'''

import asyncio
import typing
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    s_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    e_time = time.time()
    elapsed_time = e_time - s_time

    return elapsed_time
