import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#This code was modified to xor hex strings, taken from https://stackoverflow.com/questions/11119632/bitwise-xor-of-hex-numbers-in-python from user rarieg
def xor(X, Y):    
    return "".join(["%x" % (int(a,16) ^ int(b,16)) for (a, b) in zip(X, Y)])

#Uses SHA3-256 and truncates
def truncateSHA3(txt):
    h = hashlib.sha3_256(txt).digest()
    truncate = h[len(h)-3:]
    return truncate

#implements rho method for collisions
def rhoCollide(iv):
    ivEncode = iv.encode()
    hInitial = ivEncode
    hPrime = ivEncode
    count = 0
    flag = True
    while(flag):
        hInitial = truncateSHA3(hInitial)
        hPrime = truncateSHA3(truncateSHA3(hPrime))
        count += 1
        #Comment out line below to reduce print statements if necessary
        print("Iteration: {}, h = {}, h' = {}".format(count,hInitial,hPrime))
        if(hInitial == hPrime):
            flag = False
            print("Collision on iteration {}.".format(count))
    return

def main():
    print("Rho collision method \n")
    rhoCollide('000000000000000000000000')

main()