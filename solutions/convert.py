#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Writing short code
metadoc: Define a function named convert that takes a list of numbers as its only parameter and returns a list of each
         number converted to a string.
         For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
license: None
"""


def convert(lst):
    return [str(i) for i in lst]
