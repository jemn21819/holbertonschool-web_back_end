#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
from functools import wraps
from typing import Callable
import redis
import requests

r = redis.Redis()


def count_cache(method: Callable) -> Callable:
    """ count_cache """

    @wraps(method)
    def wrapper(*args):
        """ Wrapper """
        key = f"count:{args[0]}"
        r.incr(key, 1)
        r.setex("result", 10, r.get(key))
        return method(*args)
    return wrapper


@count_cache
def get_page(url: str) -> str:
    """ get_page """
    response = requests.get(url)
    return response.text
