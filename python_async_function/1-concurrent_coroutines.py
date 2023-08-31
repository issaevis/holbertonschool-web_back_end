#!/usr/bin/env python3
''' async module'''
import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''async for list'''
    value_list: List[float] = []
    all_list: List[float] = []

    for i in range(n):
        value_list.append(wait_random(max_delay))
    for task in asyncio.as_completed(value_list):
        result = await task
        all_list.append(result)
    return all_list
