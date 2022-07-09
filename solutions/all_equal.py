#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; All Equal
metadoc: Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
         For example, calling all_equal([1, 1, 1]) should return True.
license: None
"""


def all_equal(lst):
    return all(item1 == item2 for item1 in lst for item2 in lst)
