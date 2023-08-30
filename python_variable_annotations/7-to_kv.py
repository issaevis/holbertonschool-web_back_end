#!/usr/bin/env python3
from typing import List, Union
'''type annotated function'''


T : [int, float]

def to_kv(k: str,v: T) -> tuple:
    