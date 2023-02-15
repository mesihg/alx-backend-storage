#!/usr/bin/env python3
"""Task 5 module"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Caches output of fetched data"""
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper for decorator """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Return the content of a URL after caching the response"""
    req = requests.get(url)
    return req.text
