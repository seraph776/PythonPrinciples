#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Palindrome
metadoc: A string is a palindrome when it is the same when read backwards.
         For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome,
         because "abcd" != "dcba".
         Write a function named palindrome that takes a single string as its parameter. Your function should return
         True if the string is a palindrome, and False otherwise.
license: None
"""


def palindrome(s):
    return s == s[::-1]
