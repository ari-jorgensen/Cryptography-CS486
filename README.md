File: Cipher.py
Author: Ariana Jorgensen

This program can either encrypt or decrypt a file. 
User will choose whether they want to encrypt or 
decrypt. For encryption, user will either specify
the encryption algorithm they wish to use, otherwise
the Caesar cipher will be used as default. Results will
be stored in a .txt file. Name of the file will be the 
original file name with _result appended to the end 
(i.e., if file is "file.txt", result filewill be 
"file_result.txt")

USAGE: python ./Cipher.py -e | -d [-c | -p | .....] 
User will be prompted for file name when program begins.
Encryption(-e) or decryption(-d) flags are required, 
specifing algorithm is not. 

NOTE: For simplicity, all characters are converted to lowercase