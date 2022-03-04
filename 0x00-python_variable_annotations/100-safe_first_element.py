#!/usr/bin/env python3
"""
safe_first_element annotated function
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element annotated function
    """
    if lst:
        return lst[0]
    else:
        return None
