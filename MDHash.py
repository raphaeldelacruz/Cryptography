from Crypto.Random import get_random_bytes
from simon import SimonCipher
import math
from binascii import hexlify

#Retrieved from https://pythonexamples.org/python-split-string-into-specific-length-chunks/, Creates 16 bit blocks of a message
def makeBlocks(messageString,size):
    blocks = []
    i = 0
    length = size
    while i < len(messageString):
        if i+length < len(messageString):
            blocks.append(messageString[i:i+length])
        else:
            blocks.append(messageString[i:len(messageString)])
        i += length
    return blocks

#Retrieved from https://www.daniweb.com/programming/software-development/code/221031/string-to-bits
def a2bits(bytes):
    """Convert a sequence of bytes to its bits representation as a string of 0's and 1's
    This function needs python >= 2.6"""
    return bin(int(b"1" + hexlify(bytes), 16))[3:]

#Retrieved from https://stackoverflow.com/questions/9916334/bits-to-string-python
def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

#Pads block depending on how much padding is needed
def padBlock(block,size):
    newBlock = a2bits(block.encode('iso-8859-1'))
    lenBlock = len(newBlock)
    newBlock = "1"+bin(lenBlock)[2:]
    if(len(block) == size):
        return block
    else:
        while len(newBlock) < size*8:
            newBlock = newBlock[:-1*lenBlock] + "0" + newBlock[-1*lenBlock:]
    blockBits = bits2a(newBlock)
    return blockBits

#Implements DM Compression on a message block
def DM(block, cv):
    return SimonCipher(int(block.encode('iso-8859-1').hex(),16),128,128).encrypt(cv) ^ cv

def MD(hInitial, message):
    messageBlock = makeBlocks(message,16)
    messageBlock = padBlock(messageBlock[-1],16)
    for i in range(len(messageBlock)):
        if i == 0:
            compression = DM(messageBlock[i],16)
        else:
            compression = DM(messageBlock[i],compression)
    hexCompress = hex(compression)[2:]
    return hexCompress

def main():
    print("MD Hash Function using D-M compression")
    message = "This is a message that will go through M-D"
    hInit = bytes.fromhex("00000000000000000000000000000000")
    hashMessage = MD(hInit,message)
    print("This is the message that will undergo the M-D function: {}".format(message))
    print("This is the initial value we use: {}".format(hInit))
    print("This is the resultant hashed message: {}".format(hashMessage) )

main()