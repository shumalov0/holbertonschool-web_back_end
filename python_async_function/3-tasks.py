#!/usr/bin/env python3
""" returns create_task """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''returns create task'''
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1
