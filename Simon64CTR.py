from Crypto import Random
from Crypto.Random import get_random_bytes
from simon import SimonCipher

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

#Retrieved from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

#Retrieved from https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

#Encryption using Simon64/128
def encryptSimon(key,nonce,messageBlocks):
    ctxt = []
    intKey = int(key,16)
    cipher = SimonCipher(intKey, block_size=64, key_size=128, mode='CTR', counter =1, init = int(nonce,16))
    for i in range(len(messageBlocks)):
        blocktxt = bytes.fromhex(hex(cipher.encrypt(int(messageBlocks[i].encode("iso-8859-1").hex(), 16)))[2:].rjust(16,"0")).decode("iso-8859-1")
        ctxt.append(blocktxt)
    return "".join(ctxt)

#Decryption using Simon64/128
def decryptSimon(key,nonce,messageBlocks):
    ptxt = []
    intKey = int(key,16)
    cipher = SimonCipher(intKey, block_size=64, key_size=128, mode='CTR', counter =1, init = int(nonce,16))
    for i in range(len(messageBlocks)):
        blocktxt = bytes.fromhex(hex(cipher.decrypt(int(messageBlocks[i].encode("iso-8859-1").hex(), 16)))[2:].rjust(16,"0")).decode("iso-8859-1")
        ptxt.append(blocktxt)
    return "".join(ptxt)

def main():
    print("Simon64 CTR mode")
    simonKey = get_random_bytes(16).hex()
    print("Here is the key used for the simon cipher: {}".format(simonKey))
    simonNonce = get_random_bytes(8).hex()
    print("Here is the nonce used for the simon cipher: {}".format(simonNonce))
    message = "I can't think of a message, so I am just typing something until it seems to be long enough okay."
    print("Here is the message we are encrypting: {}".format(message))
    ctxt = encryptSimon(simonKey,simonNonce,makeBlocks(message,8))
    print("Here is the generated ciphertext: {}".format(ctxt.encode('iso-8859-1').hex()))
    ptxt = decryptSimon(simonKey,simonNonce,makeBlocks(ctxt,8))
    print("Here is the plaintext: {}".format(ptxt))
    hashKey = get_random_bytes(16).hex()
    print("The following message should be True if the plaintext is the same as the original message: {}".format(message == ptxt))

main()