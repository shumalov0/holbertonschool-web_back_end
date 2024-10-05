#!/usr/bin/env python3
'''
Description: function make_multiplier that takes
a float multiplier as argument and returns a
function that multiplies a float by multiplier.
Arguments: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns function'''
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
