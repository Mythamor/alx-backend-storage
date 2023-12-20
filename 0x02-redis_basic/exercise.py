#!/usr/bin/env python3

"""
Module: exercise.py
        0. Writing strings to Redis
"""


import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """
    class Cache

    Methods:__init__ 
            store
            get
            get_str
            get_int
    """
    def  __init__(self):
        """
        store an instance of the Redis client as a private variable
        and flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, 
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """
        take a key string argument and an optional Callable argument
        This callable will be used to convert data back to desired format
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
        

    def get_str(self, key: str) -> str:
        """
        automatically parametrize Cache.get with correct conversion function
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """
        automatically parametrize Cache.get with correct conversion function
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value

