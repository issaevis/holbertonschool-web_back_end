#!/usr/bin/env python3
'''defines and annotates values'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return a sum of floats in a list'''

    sum = 0
    for number in input_list:
        sum = sum + number

    return sum
