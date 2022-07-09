#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Add/Remove Dots
metadoc: Define a function named count that takes a single parameter. The parameter is a string.
         The string will contain a single word divided into syllables by hyphens
license: None
"""


def count(s):
    s = s.split('-')
    return len(s)
