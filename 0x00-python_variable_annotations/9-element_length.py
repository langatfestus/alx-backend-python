#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

{'lst': typing.Iterable[typing.Sequence], 'return': \
    typing.List[typing.Tuple[typing.Sequence, int]]}
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return list of tuples, each tuple containing a sequence and its length
    """
    return [(i, len(i)) for i in lst]
