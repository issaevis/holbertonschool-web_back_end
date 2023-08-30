#!/usr/bin/env python3
'''async function module'''
import asyncio
from random import triangular


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    '''async func that returns a list with the wait-times'''
    task = asyncio.create_task(wait_random())
    lst = []
    for i in range(n):
        num = wait_random(max_delay)
        await task
        lst.append(num)
    return lst
