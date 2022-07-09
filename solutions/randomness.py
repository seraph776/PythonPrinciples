#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Randomness
metadoc: Define a function, random_number, that takes no parameters. The function must generate a random integer
         between 1 and 100, both inclusive, and return it. Calling the function multiple times should (usually)
         return different numbers.
         For example, calling random_number() some times might first return 42, then 63, then 1.
license: None
"""

from random import randrange


def random_number():
    """Returns a random number from 1-100 inclusive."""
    return randrange(1, 101)
