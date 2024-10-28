#!/usr/bin/env python3
"""index_range function that returns a tuple containing the start index and
end index of the current page."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters (page and page_size)."""
    return ((page - 1) * page_size, page * page_size)
