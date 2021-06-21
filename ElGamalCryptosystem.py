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
    print("Shared Secret")
    p = 20876441
    g = 5
    M1 = 20192834
    C1 = 9916780
    C2 = 5260862
    #Calculate inverse of C2 so that we can find E, because then we can find d by finding the modular inverse of E in mod p
    invC2 = modinv(C2,p)
    print("Here is the inverse of C2 in modulo p = 20876441: {}".format(invC2))
    #M=E*C2 mod p, so we want to solve for E
    E = M1 * invC2 % p
    print("Here is the value of e: {}".format(E))
    D = modinv(E,p)
    print("Here is Bob's shared secret value: {}".format(D))

    print("\nRecover message")
    #Finding the unique nonce from previous message to find shared secret value, using D=C1^X=g^(X*Y) mod p, we can ignore X here for now
    for y in range(1,p-1):
        if pow(g,y,p) == C1:
            Y1 = y
            break
    print("Here is the value of the unique nonce Y1: {}".format(Y1))
    #Now we do the same as above except we include X to find shared secret
    for x in range(1,p-1):
        if pow(g,x*Y1,p) == D:
            X = x
            break
    print("Here is the secret key: {}".format(X))
    C1 = 7350174
    C2 = 13786334
    #We can find the shared secret, which we can then use to find M because C2=M*(h^Y) mod p
    h = pow(g,X,p)
    print("Here is the value of h: {}".format(h))
    #Find the nonce y2
    for y in range(1,p-1):
        if pow(g,y,p) == C1:
            Y2 = y
            break
    print("Here is the value of the unique nonce Y2: {}".format(Y2))
    D = pow(h,Y2,p)
    print("Here is the shared secret: {}".format(D))
    #M=E*C2 mod p, E = modinv(D,p)
    M2 = C2 * modinv(D,p) % p
    print("Here is the value of M2: {}".format(M2))

    print("\nMessage encryption")
    #C1=g^Y mod p, and C2=M*(h^Y) mod p
    M3 = 12345
    C1M3= 8698838
    C2M3 = 17288353
    M4 = 382695
    factor = int(M4/M3)
    #C1=g^Y mod p
    #Malleability issues means that the nonce is reused, so C1 of M3 is the C1 of M4
    C1M4 = C1M3
    #C2=M*(h^Y) mod p
    #C2M3 = M3 * h^y mod p and M4 = M3 * factor => C2M4 = M3 * factor * h^y mod p, so C2M4 = factor * C2M3 mod p
    C2M4 = factor * C2M3 % p
    print("Here is the encryption of M4: (C1,C2) = ({},{})".format(C1M4,C2M4))

main()