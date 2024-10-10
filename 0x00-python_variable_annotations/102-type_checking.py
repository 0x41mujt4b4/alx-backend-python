#!/usr/bin/env python3
# Type annotation module of zoom_array function
from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    # Return a tuple of the list zoomed in by a factor
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
