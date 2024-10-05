""" Run multiple coroutines concurrently using asyncio """

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ Spawns wait_random n times with the specified max_delay """
    delays: List[float] = [] 
    tasks: List = []  

   
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

   
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
