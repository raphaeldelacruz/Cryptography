from Crypto.Util import number
from sympy.ntheory import factorint
import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def encryptPaillier(M,nonce,p,q):
    N = p*q
    g = N + 1
    return pow(g,M, pow(N,2)) * pow(nonce,N,pow(N,2)) % pow(N,2)

def decryptPaillier(C,p,q):
    N = p*q
    #Just incase the very rare case of generating p = q, must calculate phi differently
    if(p == q):
        phi = (p-1)*p
    else:
        phi = (p-1)*(q-1)
    Q = modinv(phi,N)
    D = pow(C,phi*Q,pow(N,2))
    E = int((D-1)/N)
    #Should be E * Q % N by the assignment but it doesn't work when multiplying by Q
    return E % N

def main():
    print("Paillier encryption and decryption")
    p = number.getPrime(16)
    q = number.getPrime(16)
    N = p * q
    g = N+1
    print("Here is the value of p: {}".format(p))
    print("Here is the value of q: {}".format(q))
    print("Here is the value of N: {}".format(N))
    print("Here is the value of g: {}".format(g))
    #Generating a random message value
    M = random.randint(0,N-1)
    #nonce is the R value in the slides
    nonce = random.randint(0,N-1)
    print("Here is the value of message: {}".format(M))
    print("Here is the value of the nonce: {}".format(nonce))
    ctxt = encryptPaillier(M,nonce,p,q)
    print("Here is the value of the ctxt: {}".format(ctxt))
    ptxt = decryptPaillier(ctxt,p,q)
    print("Here is the value of the ptxt: {}".format(ptxt))
    print("The following will be true if all of our values are correct: {}".format(M == ptxt))

    print("\nFinding plaintext")
    C = 2408522148575687340805180772
    N2 = 7905547463165041131990033721
    N = int(pow(N2,.5))
    print("This is the value of N: {}".format(N))
    factors = factorint(N)
    factorList = list(factors.keys())
    p = factorList[0]
    q = factorList[1]
    print("Here is the value of p: {}".format(p))
    print("Here is the value of q: {}".format(q))
    ptxt = decryptPaillier(C,p,q)
    print("Here is the value of the ptxt: {}".format(ptxt))

    print("\nPaillier mallebability: Can be forged!")
    C1=2726070680403153614394063339 
    M1=5
    C2=5866866636167850787431170831
    M2=7
    M3=12
    N2 = 7905547463165041131990033721
    N = int(pow(N2,.5))
    forgedCtxt = (C1 * C2) % N2
    print("Here is the value of the forged ctxt: {}".format(forgedCtxt))
    factors = factorint(N)
    factorList = list(factors.keys())
    p = factorList[0]
    q = factorList[1]
    print("Here is the value of p: {}".format(p))
    print("Here is the value of q: {}".format(q))
    ptxt = decryptPaillier(forgedCtxt,p,q)
    print("Here is the value of forged ptxt: {}".format(ptxt))
    print("The following will be true if all of our values are correct: {}".format(M3 == ptxt))


main()
