#!/usr/bin/env python3
"""
zoom_array annotated function
"""
from typing import Union, Any, Mapping, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array annotated function
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
