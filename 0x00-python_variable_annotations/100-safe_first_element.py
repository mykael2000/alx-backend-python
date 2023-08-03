#!/usr/bin/env python3
'''first element in a sequence
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''get the first element in a sequence
    '''
    if lst:
        return lst[0]
    else:
        return None
