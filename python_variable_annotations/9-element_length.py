#!/usr/bin/env python3
'''
Auqment function do duct type
Arguments: lst: iterable[sequence]
'''

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns tuple in list'''
    return [(i, len(i)) for i in lst]
