#!/usr/bin/env python3
''' Run multiple coroutines concurrently with asyncio '''
import asyncio
from typing import List

# Import the wait_random function from the previous file/module
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    '''
    float time random
    '''
    delays: List[float] = []
    tasks: List = []

    # Create 'n' tasks to run wait_random concurrently
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    # Collect results as tasks complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
        
    return delays
