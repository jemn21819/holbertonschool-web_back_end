#!/usr/bin/env python3
"""
sum_mixed_list annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list return sum of list
    """
    return float(sum(mxd_lst))
