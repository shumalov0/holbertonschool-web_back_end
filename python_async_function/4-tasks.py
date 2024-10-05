#!/usr/bin/env python3
"""
returns create_task
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        float time random
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
