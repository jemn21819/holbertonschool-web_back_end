#!/usr/bin/env python3
"""
0x0B. Redis basic
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """ Incrementing values"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Storing lists"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """Retrieving lists"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """Cache class"""

    def __init__(self):
        """ constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Writing strings to Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """Reading from Redis and recovering original type"""
        if key:
            result = self._redis.get(key)
            if fn:
                return fn(result)
            else:
                return result

    def get_str(self, key: str) -> str:
        """ get_str """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """get_int """
        return self.get(key, int)
