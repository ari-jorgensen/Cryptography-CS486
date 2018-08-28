# File: PolyAlpha.py
# Author: Ariana Jorgensen
# This program handles the encryption and decryption 
# of a file using a polyalphabetic cipher.
# NOTE #1: For simplicity, all characters are converted to lowercase
# NOTE #2: I created this algorithm to work by line, i.e. shift
# is based on that letter's index in regards to the line. Therefore,
# the first letter of a line will be shifted by 1 character, the 
# second by 2, etc. The counter resets when a new line begins.

alpha = 'abcdefghijklmnopqrstuvwxyz'

def polyEncrypt(line):
	polyLine = ''
	polyWord = ''
	shift = 1
	for word in line:
		for char in word:
			try: 
				char = char.lower()
				ind = (alpha.index(char))
				newInd = (ind + shift) % 26
				newChar = alpha[newInd]
				polyWord += newChar
				shift += 1
			except ValueError:
				polyWord += char
		polyLine += polyWord
		polyWord = ''
	return polyLine

def polyDecrypt(line):
	normalLine = ''
	normalWord = ''
	shift = 1
	for word in line:
		for char in word:
			try:
				char = char.lower()
				ind = alpha.index(char)
				newInd = (ind - shift) % 26
				newChar = alpha[newInd]
				normalWord += newChar
				shift += 1
			except ValueError:
				normalWord += char
		normalLine += normalWord
		normalWord = ''
	return normalLine



