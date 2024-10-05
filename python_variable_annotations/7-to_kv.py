#!/usr/bin/env python3
'''
Description: function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
Arguments: k: string
v : int or float
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return tuple of str and float'''
    return k, v**2
