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

        assert index is None or index in range(0, len(self.dataset()))
        assert type(page_size) == int and page_size > 0

        dataset: List[List] = []
        ids = self.indexed_dataset()
        k: List[int] = []
        count: int = 0
        data: List[List] = []
        result: Dict = {}
        indexes: List = [key for key in ids.keys()]
        temp_index: Union[None, int] = index

        if index is None:
            temp_index = 0

        for key in self.indexed_dataset().keys():
            if key >= temp_index:
                if count == page_size + 1:
                    break
                dataset.append(self.indexed_dataset()[key])
                k.append(key)
                count += 1

        if len(dataset) == page_size + 1 and page_size > 1:
            if index is None:
                data = dataset[:-1]
                result.update({
                    'index': None,
                    'data': data,
                    'page_size': page_size,
                    'next_index': k[-1]
                })
            else:
                data = dataset[:-1]
                result.update({
                    'index': index,
                    'data': data,
                    'page_size': page_size,
                    'next_index': k[-1]
                })
        else:
            if index == indexes[-1] or page_size == 1:
                result.update({
                    'index': index,
                    'data': dataset[0],
                    'page_size': page_size,
                    'next_page': None
                })
            else:
                result.update({
                    'index': index,
                    'data': dataset[:-1],
                    'page_size': page_size,
                    'next_page': None
                })
        return result
