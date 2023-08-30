#!/usr/bin/env python3
'''type annotated function'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''func that returns a tuple'''
    ret = (k, v**2)

    return ret
