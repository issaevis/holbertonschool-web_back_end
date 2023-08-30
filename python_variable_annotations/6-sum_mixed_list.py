#!/usr/bin/env python3
from typing import List, Union
'''type annotated function'''


T = List[Union[float, int]]

def sum_mixed_list(mxd_lst: T) -> float:
    sum = 0
    for number in mxd_lst:
        sum += number
    return sum
