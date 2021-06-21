import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#This code was modified to xor hex strings, taken from https://stackoverflow.com/questions/11119632/bitwise-xor-of-hex-numbers-in-python from user rarieg
def xor(X, Y):    
    return "".join(["%x" % (int(a,16) ^ int(b,16)) for (a, b) in zip(X, Y)])

def main():

    print("CBC-MAC Construction \n")
    key = get_random_bytes(16)
    m1 = "There are no tricks up my sleeve"
    m2 = "I am trying to construct CBC-MAC"
    print("Here are the messages we wish to encrypt and then authenticate:")
    print("Message 1: {}".format(m1))
    print("Message 2: {}".format(m2))

    iv = bytes.fromhex("00000000000000000000000000000000")
    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    ctxt1 = cipher1.encrypt(m1.encode("iso-8859-1"))
    print("\nHere is the ciphertext: {}".format(ctxt1.hex()))
    t1 = ctxt1[len(ctxt1)-16:]
    cipher1 = AES.new(key,AES.MODE_CBC,iv)
    ptxt1 = cipher1.decrypt(ctxt1).decode('iso-8859-1')
    print("Here is the decrypted ciphertext (original plaintext): {}".format(ptxt1))
    print("This is the tag of the message: {}".format(t1))
    print("This is the length of the message: {}".format(len(m1)))
    print("This is the length of the tag: {}".format(len(t1)))

    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    ctxt2 = cipher2.encrypt(m2.encode("iso-8859-1"))
    print("\nHere is the ciphertext: {}".format(ctxt2.hex()))
    t2 = ctxt2[len(ctxt1)-16:]
    cipher2 = AES.new(key,AES.MODE_CBC,iv)
    ptxt2 = cipher2.decrypt(ctxt2).decode('iso-8859-1')
    print("Here is the decrypted ciphertext (original plaintext): {}".format(ptxt2))
    print("This is the tag of the message: {}".format(t2))
    print("This is the length of the message: {}".format(len(m2)))
    print("This is the length of the tag: {}".format(len(t2)))

    print("\nHere we will create a forged message and tag.")
    t3 = bytearray.fromhex(xor(m2.encode('iso-8859-1').hex(), t1.hex())).decode('iso-8859-1')
    m3 = m1 + t3
    print("Here is the forged message: {}".format(m3))
    print("Here is the forged tag: {}".format(t3))



main()