#!/usr/bin/env python3
"""
annotated a function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function annotated
    """
    return [(i, len(i)) for i in lst]
