# File: SimpleSubstitution.py
# Author: Ariana Jorgensen
# This program handles the encryption and decryption 
# of a file using a simple substitution cipher.
# I created this algorithm myself, only borrowing the
# randomized alphabet from the Wikipedia example
# of substitution ciphers
# NOTE: For simplicity, all characters are converted to lowercase

# Regular alphabet & randomized substitution
# alphabet to be used for encyrption/decryption
alpha = 'abcdefghijklmnopqrstuvwxyz'
subAlpha = 'vjzbgnfeplitmxdwkqucryahso'

def simpleSubEncrypt(line):
	subLine = ''
	subWord = ''
	for word in line:
		for char in word:
			try:
				char = char.lower()
				ind = alpha.index(char)
				newChar = subAlpha[ind]
				subWord += newChar
			except ValueError:
				subWord = char
		subLine += subWord
		subWord = ''
	return subLine

def simpleSubDecrypt(line):
	normalLine = ''
	normalWord = ''
	for word in line:
		for char in word:
			try:
				char = char.lower()
				ind = subAlpha.index(char)
				newChar = alpha[ind]
				normalWord += newChar
			except ValueError:
				normalWord += char
		normalLine += normalWord
		normalWord = ''
	return normalLine
