#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Middle Letter
metadoc: The aim of this challenge is, given a dictionary of people's online status, to count the number of
         People who are online. The dictionary used: statuses = {"Alice": "online","Bob": "offline","Eve": "online",}
license: None
"""


def online_count(d):
    """Counts the number of user's online in a dictionary."""
    return sum([1 for value,  value in d.items() if value == 'online' ])
