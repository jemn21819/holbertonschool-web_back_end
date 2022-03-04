#!/usr/bin/env python3
"""
make_multiplier annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier functin return multplies by mu;plier
    """
    def mul(x: float) -> float:
        return x * multiplier
    return mul
