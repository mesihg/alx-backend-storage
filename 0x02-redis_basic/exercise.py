#!/usr/bin/env python3
"""Task 0 module"""
import redis
import uuid
from typing import Union



class Cache:
    """Represent an object that can be stored in a Redis data storage"""
    def __init__(self) -> None:
        """Initializes a Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
