#!/usr/bin/env python3
""" function measures wait_n execution time """
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''to measure time'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n
