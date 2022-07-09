#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Type Check
metadoc: Write a function named only_ints that takes two parameters. Your function should return True if both
         parameters are integers, and False otherwise.
         For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
license: None
"""

def only_ints(a, b):
    return type(a) == int and type(b) == int
