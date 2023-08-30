#!/usr/bin/env python3
'''async function module'''

import asyncio
from random import triangular


async def wait_random(max_delay: int=10) -> float:
    '''async func that returns the delay time in float'''
    num = triangular(0, max_delay)
    await asyncio.sleep(num)
    return num
