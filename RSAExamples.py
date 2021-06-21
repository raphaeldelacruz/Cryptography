from sympy import factorint
import math

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

def main():
    print("RSA")
    e = 17
    print("Here is the value of e: {}".format(e))
    N = 38210080753993935337519
    print("Here is the value of N: {}".format(N))
    C = 29202530725918700842079
    print("Here is the value of C: {}".format(C))
    #Using library function that quickly finds factors of N
    factors = factorint(N)
    factorList = list(factors.keys())
    #There should only be two prime factors for this cryptosystem
    p = factorList[0]
    print("Here is the value of p: {}".format(p))
    q = factorList[1]
    print("Here is the value of q: {}".format(q))
    phi = (p-1) * (q-1)
    print("Here is the value of phi that is (p-1)(q-1): {}".format(phi))
    d = modinv(e,phi)
    print("Here is the inverse of d, the private key: {}".format(d))
    M = pow(C,d,N)
    print("Here is the value of M: {}".format(M))
    #Encrypting M using the public key to verify it is correct
    ctxtVerify = pow(M,e,N)
    print("The following will be true if all of our values are correct: {}".format(C==ctxtVerify))

    print("\nCube Root Attack")
    e = 3
    N = 237586812181653994808797835837127641
    C = 14621362594515611576696983236378624
    print("Here is the value of e: {}".format(e))
    print("Here is the value of N: {}".format(N))
    print("Here is the value of C: {}".format(C))
    #Using cube root attack
    M = int(round(pow(C,1/3)))
    print("Here is the value of M: {}".format(M))
    ctxtVerify = pow(M,e,N)
    print("The following will be true if all of our values are correct: {}".format(C==ctxtVerify))

    print("\nOne Prime RSA")
    e = 65537
    N = 782411451307002751974547518481
    C = 750555647839236294597477460513
    print("Here is the value of e: {}".format(e))
    print("Here is the value of N: {}".format(N))
    print("Here is the value of C: {}".format(C))
    p = int(pow(N,.5))
    print("Here is the value of p: {}".format(p))
    phi = (p) * (p-1)
    print("Here is the value of phi: {}".format(phi))
    d = modinv(e,phi)
    print("Here is the value of the private exponent, d: {}".format(d))
    M = pow(C,d,N)
    print("Here is the value of M: {}".format(M))
    ctxtVerify = pow(M,e,N)
    print("The following will be true if all of our values are correct: {}".format(C==ctxtVerify))

main()