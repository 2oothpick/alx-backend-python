#!/usr/bin/env python3
"""
Duck typing
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns elements of the list with its length
    """
    return [(i, len(i)) for i in lst]
