#!/usr/bin/env python3
'''async function module'''
import asyncio
from random import triangular
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    total_time = 0

    loop = asyncio.get_event_loop()

    for _ in range(n):
        start_time = time.time()

        result = loop.run_until_complete(wait_n(n, max_delay))

        end_time = time.time()
        total_time += (end_time - start_time)

    average_time = total_time / n
    return average_time
