#!/usr/bin/env python3
'''module that annotates values to functions'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function that uses annotation'''

    sum = 0
    for number in mxd_lst:
        sum += number
    return sum
