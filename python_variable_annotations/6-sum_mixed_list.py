#!/usr/bin/env python3
'''
Description: function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
Arguments: mxd_lst: list of integers and floats
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns sum of list'''
    return sum(mxd_lst)
