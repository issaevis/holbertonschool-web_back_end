#!/usr/bin/env python3
'''async module'''

import asyncio
import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''returns a list of floats to the main'''

    return [i async for i in async_generator()]
