# File: Caesar.py
# Author: Ariana Jorgensen
# This program handles the encryption and decryption 
# of a file using the Caesar cipher. I made the shift
# a constant of 4, however this would technically
# work with any shift # as I use mod 26 to ensure
# that the index remains in the alphabet.
# NOTE: For simplicity, all characters are converted to lowercase

alpha = 'abcdefghijklmnopqrstuvwxyz'

# Function to encrypt file using the 
# Caesar cipher. Shift = 3
def caesarCipherEncrypt(line):
    caesarLine = ''
    caesarWord = ''
    for word in line:
        for char in word:
            try:
                char = char.lower()
                ind = (alpha.index(char) + 3) % 26
                caesarWord += alpha[ind]
            except ValueError:
                caesarWord += char
        caesarLine += caesarWord
        caesarWord = ''
    return caesarLine

# Function to decrypt file that was encrypted
# using the Caesar cipher. Shift = 3
def caesarCipherDecrypt(line):
    normalLine = ''
    normalWord = ''
    for word in line:
        for char in word:
            try:
            	char = char.lower()
                ind = (alpha.index(char) - 3) % 26
                normalWord += alpha[ind]
            except ValueError:
                normalWord += char
        normalLine += normalWord
        normalWord = ''
    return normalLine