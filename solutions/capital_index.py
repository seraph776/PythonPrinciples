#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Capital Index
metadoc: Write a function named capital_indexes. The function takes a single parameter, which is a string.
         Your function should return a list of all the indexes in the string that have capital letters.
         For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
license: None
"""


def capital_indexes(s):
    return [idx for idx, item in enumerate(s) if item.isupper()]
