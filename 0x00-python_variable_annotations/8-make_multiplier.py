#!/usr/bin/env python3
'''function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier function
    '''
    return lambda x: x * multiplier
