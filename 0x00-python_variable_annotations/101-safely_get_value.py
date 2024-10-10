from typing import TypeVar, Mapping, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    if key in dct:
        return dct[key]
    else:
        return default