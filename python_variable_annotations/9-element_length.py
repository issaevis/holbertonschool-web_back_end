#!/usr/bin/env python3
'''type annotated function'''
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns something complicated that I can't explain
    ATM because I am on 4 hours of sleep'''
    return [(i, len(i)) for i in lst]
