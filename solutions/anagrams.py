#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Anagrams
metadoc: Two strings are anagrams if you can make one from the other by rearranging the letters.
         Write a function named is_anagram that takes two strings as its parameters. Your function should return
        True if the strings are anagrams, and False otherwise.
license: None
"""


def is_anagram(s1, s2):
    """Returns True if s1 and s2 are anagrams"""
    d1 = {k:s1.count(k) for k in s1}
    d2 = {k:s2.count(k) for k in s2}
    return d1 == d2
