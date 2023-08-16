#!/usr/bin/env python3
<<<<<<< HEAD
'''Task 0's module.
=======
'''Async Generator
>>>>>>> e1bda4bd8d622b937ff88f4c8ef0b43ef7ded73d
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
