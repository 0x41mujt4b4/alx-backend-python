#!/usr/bin/env python3
"""Type annotation module of safely_get_value function"""
from typing import TypeVar, Mapping, Optional, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Return the value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
