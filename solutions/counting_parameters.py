#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Counting parameters
metadoc: Define a function param_count that takes a variable number of parameters. The function should return the
         number of arguments it was called with.
         For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
license: None
"""


def param_count(*n):
    return len(n)
