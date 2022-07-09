#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Thousands separator
metadoc: Write a function named format_number that takes a non-negative number as its only parameter.
         Your function should convert the number to a string and add commas as a thousands separator.
         For example, calling format_number(1000000) should return "1,000,000".
license: None
"""


def format_number(n):
    n = reversed(list(str(n)))
    output = ''.join([',' + el if i % 3 == 0 else el for (i, el) in enumerate(n)])
    for i, el in enumerate(n):
        if i % 3 == 0:
            output += ',' + el
        else:
            output += el
    return output[::-1][:-1]
