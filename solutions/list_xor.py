#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; List XOR
metadoc: Define a function named list_xor. Your function should take three parameters: n, list1 and list2.
         Your function must return whether n is exclusively in list1 or list2.
         In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists,
         return True.
license: None
"""


def list_xor(n, lst1, lst2):
    return n in lst1 and n not in lst2 or n in lst2 and n not in lst1
