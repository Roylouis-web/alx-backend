#!/usr/bin/env python3

"""
    Module for a function named index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
        A function named index_range that takes two
        integers: page and page_size and returns a tuple
    """

    start_index: int = (page * page_size) - page_size
    end_index: int = page * page_size

    return (start_index, end_index)
