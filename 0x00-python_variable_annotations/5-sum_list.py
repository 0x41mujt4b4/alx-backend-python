#!/usr/bin/env python3
# Type annotation module of sum_list function
from typing import List


def sum_list(input_list: List[float]) -> float:
    # Return the sum of the list of floats
    return sum(input_list)
