#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Consecutive Zeros
metadoc: The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
         Your code should find the biggest number of consecutive zeros in the string. For example, given the string:
         - "1001101000110"
         The biggest number of consecutive zeros is 3.
license: None
"""


def consecutive_zeros(s):
    counter = 0
    max_count = 0
    for i, el in enumerate(s):
        if s[i] == '1':
            counter = 0
        else:
            counter += 1
            max_count = max(max_count, counter)
