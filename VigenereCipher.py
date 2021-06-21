#Raphael Dela Cruz 2/26/21

#Using this alphabet list in order to not need to guess with unicode
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Finds position in alphabet to pull from alphabet string
def getAlphabetPosition(letter):
    return alphabet.index(letter)

#Finds letter given alphabetical number in alphabet string
def getAlphabetLetter(number):
    return alphabet[number]


def decryptVigenere(key,ctxt):
    ptxt = ""
    lenKey = len(key)
    #I lowercase all text to avoid any kind of conflict
    ctxt = ctxt.lower()
    key = key.lower()
    #Goes through each letter of ciphertext, adds ctxt position with key position, then finds new letter in alphabet. Adds to ptxt string.
    for x in range(len(ctxt)):
        position = getAlphabetPosition(ctxt[x]) - getAlphabetPosition(key[x % lenKey])
        ptxt = ptxt + getAlphabetLetter(position % 26)
    return ptxt

def encryptVigenere(key,ctxt):
    ptxt = ""
    lenKey = len(key)
    #I lowercase all text to avoid any kind of conflict
    ctxt = ctxt.lower()
    key = key.lower()
    #Goes through each letter of ciphertext, adds ctxt position with key position, then finds new letter in alphabet. Adds to ptxt string.
    for x in range(len(ctxt)):
        position = getAlphabetPosition(ctxt[x]) + getAlphabetPosition(key[x % lenKey])
        ptxt = ptxt + getAlphabetLetter(position % 26)
    return ptxt

#Performs prompts to allow user to decrypt, prints key and ciphertext followed by resulting plaintext.
def main():
    userFlag = False
    userInput = input("Would you like to decrypt?: ")
    if(userInput.lower() == "yes" or userInput.lower() == "y"):
        userFlag = True

    while(userFlag):
        userFlag = False
        keyInput = input("What is the key for decryption?: ")
        ctxtInput = input("What is the ciphertext you want to decrypt?: ")
        print(decryptVigenere(keyInput,ctxtInput))
        userInput = input("Would you like to decrypt?: ")
        if(userInput.lower() == "yes" or userInput.lower() == "y"):
            userFlag = True
    
    #Included this to be able to include the five pairs.
    #I realize I could have used a for-loop for these-- this is done in future problems.
    print("The following are five ctxt pairs to demonstrate correctness:")
    print("With key: key and ciphertext: MCZOV, we should get plaintext: cyber")
    print(decryptVigenere("key","MCZOV")) #Should be cyber 
    print("With key: encrypt and ciphertext: HREIWEM, we should get plaintext: decrypt")
    print(decryptVigenere("encrypt", "HREIWEM")) #Should be decrypt
    print("With key: security and cipertext: UVAJKWZPSTJS, we should get plaintext: cryptography")
    print(decryptVigenere("security", "UVAJKWZPSTJS")) #Should be cryptography
    print("With key: security and ciphertext: RFEARPCVOSPV, we should get plaintext: nonmalleable")
    print(decryptVigenere("error", "RFEARPCVOSPV")) #Should be nonmalleable
    print("With key: breach breach and ciphertext: BKXAERFI, we should get plaintext: attacker")
    print(decryptVigenere("breach", "BKXAERFI")) #Should be attacker

#These encrypted texts were obtained and verified using https://crypto.interactive-maths.com/vigenegravere-cipher.html
main()