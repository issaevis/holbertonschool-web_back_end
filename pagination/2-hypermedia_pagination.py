#!/usr/bin/env python3
'''simple helper function'''


import csv
import math
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''returns a list with the contents of a page'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        indexes = index_range(page, page_size)
        if indexes is None:
            return []

        start_index, end_index = indexes
        if start_index >= total_rows:
            return []

        end_index = min(end_index, total_rows - 1)
        page_data = dataset[start_index:end_index]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''returns a dict'''
        page_data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        # Calculate next_page and prev_page
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
