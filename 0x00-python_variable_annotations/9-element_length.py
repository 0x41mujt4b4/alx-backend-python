#!/usr/bin/env python3
"""Type annotation module of element_length function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the sequence and its length"""
    return [(i, len(i)) for i in lst]
