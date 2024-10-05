#!/usr/bin/env python3
''' Run multiple coroutines concurrently with asyncio '''
import asyncio
from typing import List

# Import the wait_random function from the previous file/module
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Execute wait_random 'n' times with concurrency and return sorted delays.
    '''
    tasks: List[asyncio.Task] = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    # Collect results as tasks complete in the order they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    
    # Return the delays sorted in ascending order (because tasks complete in that order)
    return sorted(delays)
