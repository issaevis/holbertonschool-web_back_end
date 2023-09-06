#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List, Dict


class Server:
        """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        '''muh dataset'''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        '''indexes and all that'''
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''asc as if this is properly documented, I AM SOOO SLEEP DEPRIVED'''
        assert index is None or (isinstance(
            index, int) and 0 <= index < len(self.indexed_dataset()))
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        total_rows = len(indexed_data)

        if index is None:
            index = 0
        elif index >= total_rows:
            return {}

        start_index = index
        end_index = min(start_index + page_size, total_rows)

        while start_index < end_index and start_index not in indexed_data:
            start_index += 1

        page_data = [indexed_data.get(
            i, []) for i in range(start_index, end_index)]

        next_index = end_index

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
