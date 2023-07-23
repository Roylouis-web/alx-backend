#!/usr/bin/env python3

"""
    Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict


class Server:
    """
        Server class to paginate a database of popular
        baby names
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """"
            Dataset indexed by sorting position, starting
            at 0
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
            returns a dictionary containing info about
            an index in a database
        """

        if index is None:
            index = 0

        assert index in range(0, len(self.dataset()))

        dataset: List[List] = []
        k: List[int] = []
        count: int = 0
        data: List[List] = []
        next_index = None

        for key in self.indexed_dataset().keys():
            if key >= index:
                if count == page_size + 1:
                    break
                dataset.append(self.indexed_dataset()[key])
                k.append(key)
                count += 1
        if len(dataset) == page_size + 1:
            data = dataset[:-1]
            next_index = k[-1]
        else:
            data = dataset

        return {
                'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': next_index
            }
