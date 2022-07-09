#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Middle Letter
metadoc: Write a function named mid that takes a string as its parameter. Your function should extract and return
         the middle letter. If there is no middle letter, your function should return the empty string.
         For example, mid("abc") should return "b" and mid("aaaa") should return "".
license: None
"""


def mid(s):
    return "" if len(s) % 2 == 0 else s[(len(s)-1)//2]
