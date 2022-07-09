#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Add/Remove Dots
metadoc: Write a function named add_dots that takes a string and adds "." in between each letter.
         For example, calling add_dots("test") should return the string "t.e.s.t".
         Then, below the add_dots function, write another function named remove_dots that removes all dots from a string.
         For example, calling remove_dots("t.e.s.t") should return "test".
         If both functions are correct, calling remove_dots(add_dots(string)) should return back the original
        string for any string.
license: None
"""


def add_dots(s):
    s = list(s)
    return '.'.join(s)


def remove_dots(s):
    s = s.replace('.', '')
    return s
