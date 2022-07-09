#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Boolean and
metadoc: Define a function named triple_and that takes three parameters and returns True only if they are all
         True and False otherwise.
license: None
"""


def triple_and(a, b, c):
    return all([a, b, c])
