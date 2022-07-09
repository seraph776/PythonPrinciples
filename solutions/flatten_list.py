#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Flatten a List
metadoc: Write a function that takes a list of lists and flattens it into a one-dimensional list.
         Name your function flatten. It should take a single parameter and return a list.
license: None
"""


def flatten(lst):
    return sum(lst, [])
