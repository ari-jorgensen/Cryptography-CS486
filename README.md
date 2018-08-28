File: Cipher.py
Author: Ariana Jorgensen

This program can either encrypt or decrypt a file. User will choose whether they want to encrypt or 
decrypt. User will either specify the algorithm they wish to use, otherwise the Caesar cipher will be used as 
default. Results will be stored in a .txt file. User has the option to specify a name for the result file. 
If they do not wish to specify a name, the output file will be the original name of the file with either _encrypted
or _decrypted appended to the end. 

For simplicity, all characters are converted to lowercase.

USAGE: python ./Cipher.py (-e | -d) [-c | -p | -t] <file name> 
Encryption(-e) or decryption(-d) flags are required, specifing algorithm is not. 

