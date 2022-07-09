#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Anagrams
metadoc: Define a function named largest_difference that takes a list of numbers as its only parameter.
         Your function should compute and return the difference between the largest and smallest number in the list.
license: None
"""


def largest_difference(lst):
    return max(lst) - min(lst)
