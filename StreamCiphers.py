from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#This code was modified to xor hex strings, taken from https://stackoverflow.com/questions/11119632/bitwise-xor-of-hex-numbers-in-python from user rarieg
def xor(X, Y):    
    return "".join(["%x" % (int(a,16) ^ int(b,16)) for (a, b) in zip(X, Y)])

def initState(key, nonce):
    cipher = AES.new(key,AES.MODE_CBC,nonce)
    txt = cipher.encrypt(nonce)
    return txt

def updateState(previousState,nonce):
    cipher = AES.new(b'\x00'*16,AES.MODE_CBC,nonce)
    txt = cipher.encrypt(previousState)
    return txt

#Retrieved from https://pythonexamples.org/python-split-string-into-specific-length-chunks/, Creates 16 bit blocks of a message
def makeBlocks(messageString):
    blocks = []
    i = 0
    #Better to add this as an argument but for this program I only am using 16 as length
    length = 16
    while i < len(messageString):
        if i+length < len(messageString):
            blocks.append(messageString[i:i+length])
        else:
            blocks.append(messageString[i:len(messageString)])
        i += length
    return blocks

def stateCipher(key,nonce,message):
    txt = ""
    blocks = makeBlocks(message)
    initialState = initState(key,nonce)
    for i in range(len(blocks)):
        if i == 0:
            state = initialState
        else:
            state = updateState(state,nonce)
        hexBlock = blocks[i].encode('iso-8859-1').hex()
        hexState = state.hex()
        xorVal = xor(hexState,hexBlock)
        txt += xorVal
    return txt

def counterCipher(key, nonce, message):
    cipher =  AES.new(key,AES.MODE_CBC,nonce)
    txt = ""
    blocks = makeBlocks(message)
    counter = 0
    for i in range(len(blocks)):
        hexBlock = blocks[i].encode('iso-8859-1').hex()
        bytesCounter = counter.to_bytes(16, byteorder="big")
        cipherEncrypt = cipher.encrypt(key+nonce+bytesCounter).hex()
        xorVal = xor(cipherEncrypt,hexBlock)
        txt += xorVal
        counter +=1
    return txt


def main():
    mainKey = get_random_bytes(16)
    nonce = get_random_bytes(16)
    message = 'Stream ciphers generate pseudorandom bits from a key and a nonce and encrypt the plaintext by XORing it with these pseudorandom bits, similar to the one time pad'
    print("\nPart 1a): Stateful Cipher ")
    print("\nHere are the inputs: Key: {}, Nonce: {}, Message: {}".format(mainKey,nonce,message))
    ctxt = stateCipher(mainKey,nonce,message)
    ctxtString = bytes.fromhex(ctxt).decode("iso-8859-1")
    print("\nHere is the ciphertext after encrypting: {}".format(ctxt))
    ptxt = stateCipher(mainKey,nonce,ctxtString)
    ptxtString = bytes.fromhex(ptxt).decode("iso-8859-1")
    print("\nHere is the ciphertext after decrypting: {}".format(ptxtString))

    
    print("\nCounter Cipher")
    mainKeyB = get_random_bytes(16)
    nonceB = get_random_bytes(16)
    print("\nHere are the inputs: Key: {}, Nonce: {}, Message: {}".format(mainKeyB,nonceB,message))
    ctxtB = counterCipher(mainKeyB,nonceB,message)
    ctxtStringB = bytes.fromhex(ctxtB).decode('iso-8859-1')
    print("\nHere is the ciphertext after encrypting: {}".format(ctxtB))
    ptxtB = counterCipher(mainKeyB,nonceB,ctxtStringB)
    ptxtStringB = bytes.fromhex(ptxtB).decode("iso-8859-1")
    print("\nHere is the ciphertext after decrypting: {}".format(ptxtStringB))

    

main()