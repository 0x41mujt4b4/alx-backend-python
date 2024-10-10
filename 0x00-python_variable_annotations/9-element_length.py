#!/usr/bin/env python3
# Type annotation module of element_length function
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    # Return a list of tuples containing the string and its length
    return [(i, len(i)) for i in lst]
