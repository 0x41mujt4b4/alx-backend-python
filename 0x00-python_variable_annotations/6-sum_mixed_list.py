#!/usr/bin/env python3
"""Type annotation module of sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the list of mixed floats and integers"""
    return float(sum(mxd_lst))
