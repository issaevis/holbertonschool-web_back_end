#!/usr/bin/env python3
from typing import List, Union
'''type annotated function'''


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum = 0
    for number in mxd_lst:
        sum += number
    return sum
