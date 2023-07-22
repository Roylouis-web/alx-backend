#!/usr/bin/env python3

"""
    Module for a class called Server
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
        A class called Server that helps
        with the pagination of a page
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            returns a list of lists whose length is equal to
            page_size
        """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page > 0
        dataset = self.dataset()
        total_rows = len(dataset)
        total_pages = math.ceil(total_rows / page_size)

        if page not in range(1, total_pages):
            return []
        res = index_range(page, page_size)

        return [dataset[i] for i in range(res[0], res[1])]
