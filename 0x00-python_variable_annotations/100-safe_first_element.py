#!/usr/bin/env python3
"""Type annotation module of safe_first_element function"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
