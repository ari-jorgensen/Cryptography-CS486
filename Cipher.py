# File: Cipher.py
# Author: Ariana Jorgensen
# USAGE: python ./Cipher.py (-e | -d) [-c | -p | -s] <file name> 
# Encryption(-e) or decryption(-d) flags are required, 
# specifing algorithm is not. 

# Import argparse as well as classes that handle each 
# encryption/decryption algorithms
import argparse
import Caesar
import SimpleSubstitution
import PolyAlpha
import Transposition


def getArgs():
    parser = argparse.ArgumentParser(description=
        'Encrypt or decrypt a file. Must specify encryption (-e) or decryption (-d) and file name.')
    groupEorD = parser.add_mutually_exclusive_group(required=True)
    groupEorD.add_argument('-e', '--encrypt', action='store_true', help='File will be encrypted')
    groupEorD.add_argument('-d', '--decrypt', action='store_true', help='File will be decrypted')
    parser.add_argument('file', nargs=1, type=str, help='The file to be encrypted/decrypted')
    groupCipher = parser.add_mutually_exclusive_group()
    groupCipher.add_argument('-c', '--caesar', action='store_true', help='Use Caesar cipher')
    groupCipher.add_argument('-p', '--poly', action='store_true', help='Use poly-alphabetic cipher')
    groupCipher.add_argument('-s', '--substitution', action='store_true', help='Use simple substitution cipher')    
    groupCipher.add_argument('-t', '--transposition', action='store_true', help='Use transposition cipher')        
   
    return parser.parse_args()

# This function simply creates the file in which the 
# result is stored. Name is returned, file is not yet
# opened. User has the option to either chose 
def createResultFile(name, type):
    usrSpec = raw_input('Would you like to specify an output file name?[y/n]: ')
    if usrSpec == 'y':
        resultFileName = raw_input('Enter the output file name: ')
        return resultFileName
    else:
        if '_' in name:
            tmp = name.split('_')
            resultFileName = tmp[0] + type + '.txt'
        else:
            tmp = name.split(".")
            resultFileName = tmp[0] + type + '.txt'
        return resultFileName

    
def processArgs(args):
    filename = args.file[0]
    if args.encrypt:
        file = open(filename, "r")
        resultFileName = createResultFile(filename, '_encrypted')
        resultFile = open(resultFileName, "w+")
        ln = file.readlines()
        for x in ln:
            if args.caesar:
                ret = Caesar.caesarCipherEncrypt(x)
                resultFile.write(ret)
            elif args.substitution:
                ret = SimpleSubstitution.simpleSubEncrypt(x)
                resultFile.write(ret)
            elif args.poly:
                ret = PolyAlpha.polyEncrypt(x)
                resultFile.write(ret)
            elif args.transposition:
                ret = Transposition.transEncrypt(x)
                resultFile.write(ret)
            else:
                ret = Caesar.caesarCipherEncrypt(x)
                resultFile.write(ret)
    elif args.decrypt:
        file = open(filename, "r")
        resultFileName = createResultFile(filename, '_decrypted')
        resultFile = open(resultFileName, "w+")
        ln = file.readlines()
        for x in ln:
            if args.caesar: 
                ret = Caesar.caesarCipherDecrypt(x)
                resultFile.write(ret)
            elif args.substitution:
                ret = SimpleSubstitution.simpleSubDecrypt(x)
                resultFile.write(ret)
            elif args.poly:
                ret = PolyAlpha.polyDecrypt(x)
                resultFile.write(ret)
            elif args.transposition:
                ret = Transposition.transDecrypt(x)
                resultFile.write(ret)
            else:
                ret = Caesar.caesarCipherDecrypt(x)
                resultFile.write(ret)


def main():
    args = getArgs()
    processArgs(args)

if __name__ == '__main__':
    main()









