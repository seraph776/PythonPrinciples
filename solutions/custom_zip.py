#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Custom zip
metadoc: The built-in zip function "zips" two lists. Write your own implementation of this function.
         Define a function named zap. The function takes two parameters, a and b. These are lists.
         Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
         For example:

         zap(
            [0, 1, 2, 3],
            [5, 6, 7, 8]
         )

         Should return:

         [(0, 5),
         (1, 6),
         (2, 7),
         (3, 8)]
license: None
"""


def zap(a, b):
    i = 0
    mx = len(a)
    res = []

    while i < mx:
        res.append((a[i], b[i]))
        i += 1
    return res
