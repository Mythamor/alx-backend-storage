#!/usr/bin/env python3

"""
Module: exercise.py
        0. Writing strings to Redis
"""


import redis
import uuid
from typing import Union


class Cache:
    """
    class Cache

    Methods:__init__ 
            store
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
