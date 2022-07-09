#!/usr/bin/env python3
"""
created: 2022-07-09 12:30:45
@author: seraph★1001100
contact: admin@codecrypt76.com
project: Python Principles; Tic Tac Toe Input
metadoc: DThe board is represented as a 2D list:
         board = [
         ["X", "O", "X"],
         [" ", " ", " "],
         ["O", " ", " "],
         ]
        magine if your user enters "C1" and you need to see if there's an X or O in that cell on the board.
        To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check
        board[row][column]. Your task is to write a function that can translate from strings of length 2 to a tuple
        (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2
        consisting of an uppercase letter and a digit.
license: None
"""


def get_row_col(param):
    row, col = param[0], param[1]
    ht = {'1': 0, '2': 1, '3': 2, 'A': 0, 'B': 1, 'C': 2}
    return ht.get(col), ht.get(row)
