#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Dict, Any


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Constructor
        """
        self.__dataset = None

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         takes two integer arguments page with default value 1 and page_size
        with default value 10.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        return self.dataset()[index_range(page, page_size)[0]:
                              index_range(page, page_size)[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        hat takes the same arguments (and defaults) as get_page and
        returns a dictionary
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages}
        return data
