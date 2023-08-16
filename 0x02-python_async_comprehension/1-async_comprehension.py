#!/usr/bin/env python3
<<<<<<< HEAD
'''Task 1's module.
=======
'''Async Comprehensions
>>>>>>> e1bda4bd8d622b937ff88f4c8ef0b43ef7ded73d
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
