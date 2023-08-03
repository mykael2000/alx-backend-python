#!/usr/bin/env python3
'''string and int/float to turple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''string int/float to tuple conversion
    '''
    return (k, float(v**2))
