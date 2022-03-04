#!/usr/bin/env python3
"""
to_kv annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv function creat a tuple of float and str
    """
    return (k, v**2)
