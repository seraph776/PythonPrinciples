#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Double Letters
metadoc: The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
         For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical
         letters in a row.
         Define a function named double_letters that takes a single parameter. The parameter is a string.
         Your function must return True if there are two identical letters in a row in the string, and False otherwise.
license: None
"""


def double_letters(s):
    for i1, i2 in zip(s[::], s[1::]):
        if i1 == i2:
            return True
    return False
