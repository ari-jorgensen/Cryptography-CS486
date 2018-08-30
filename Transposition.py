# REPLACE WITH AN ALPHA-NUMERIC CIPHER?????

# File: Transposition.py
# Author: Ariana Jorgensen
# For this particular algorithm, I 
# borrowed the logic as well as a library
# from InventWithPython: 
# (https://inventwithpython.com/hacking/chapter9.html) and 
# (https://inventwithpython.com/hacking/chapter8.html)
# 

import pyperclip
import math

# Arbitrary value used for transposition 
# cipher. Could be any number
key = 8

def transEncrypt(line):
	transLine = [''] * key
	for col in range(key):
		pointer = col
		while pointer < len(line):
			transLine[col] += line[pointer]
			pointer += key
	return ''.join(transLine)


def transDecrypt(line):
	numCols = math.ceil(len(line) / key)
	numRows = key
	numBox = (numCols * numRows) - len(line)
	normalLine = [''] * int(numCols)
	col = 0
	row = 0

	for char in line:
		normalLine[col] += char
		col += 1

		if (col == numCols) or (col == numCols - 1 and row >= numRows - numBox):
			col = 0
			row += 1
	return ''.join(normalLine)
