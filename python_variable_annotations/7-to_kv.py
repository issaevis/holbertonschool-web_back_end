#!/usr/bin/env python3
from typing import Union
'''type annotated function'''


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''func that returns a tuple'''
    ret = (k, v**2)

    return ret
