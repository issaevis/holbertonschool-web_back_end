#!/usr/bin/env python3
'''async module'''

import asyncio
from random import triangular

async def async_generator():
    '''yields a random float'''

    for i in range(10):
        await asyncio.sleep(1)
        yield(triangular(0, 10))
