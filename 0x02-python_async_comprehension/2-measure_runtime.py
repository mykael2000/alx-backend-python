#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Executes async_comprehension 4 times and measures the
    total execution time.
    '''
<<<<<<< HEAD
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
=======
    starter = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - starter
>>>>>>> e1bda4bd8d622b937ff88f4c8ef0b43ef7ded73d
