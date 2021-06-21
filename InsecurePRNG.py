#Raphael Dela Cruz 3/8/21

def modAddedBits(byteInput):
    lenBytes = len(byteInput)
    byteSum = 0
    for i in range(lenBytes):
        byteSum += int(byteInput[i])
    return byteSum % 2

def processArray(byteArray):
    #Adds each part in the array like a string to be used for modaddedbits function
    byteString = str(byteArray[10])+ str(byteArray[12]) + str(byteArray[13]) + str(byteArray[15])
    strBits = str(modAddedBits(byteString))
    return strBits + byteArray[:15]

def prng(seed,byteNum):
    bitList = seed
    #We only need in range 8 because generating with the seed gives us 16 bits, and we only need 8 to make a byte.
    for i in range(int((byteNum+1)/2)):
        genArray = processArray(bitList)
        print("Here are randomly generated bytes: {} and {}".format(genArray[:8],genArray[8:]))
        bitList = genArray

def backtrack(output):
        #We can find the 16th index by xorring all the values that were shifted, along with the first bit which is modulo 2 of all them added
        stringVal = str(output[11]) + str(output[13])+ str(output[14]) + str(output[0])
        endValue = str(modAddedBits(stringVal))
        #Concatenate the newly found 16th index to the new output
        input = output[1:] + endValue
        print("The previous value was {}".format(input))
        return input

def main():
    print("Part a):")
    print("Input: 1110, expected output: 1, got:{}".format(modAddedBits("1110")))
    print("Input: 0011, expected: 0, got:{}".format(modAddedBits("0011")))

    print("\nPart b):")
    print("There will be a 0 in spot 11, 0 in spot 13, 1 in spot 14 and a 0 in spot 16, so expect a 0 in spot 1.")
    print("Input list: {}".format('1011010110010111'))
    print(processArray('1011010110010111'))
    print("\nThere is a 1 in spot 11, a 0 in spot 13, a 1 in spot 14 and a 1 in spot 16, so expect a 1 in spot 1")
    print("Input list: {}".format('0101011010110111'))
    print(processArray('0101011010110111'))

    print("\nPart c):")
    print("\nThis is the output for the byte seed 1011010110010111")
    prng('1011010110010111',16)
    print("\nThis is the output for the byte seed 0101011010110111")
    prng('0101011010110111',16)

    print("\n Part d):")
    print("AB09 in binary is 1010101100001001.")
    print("\nThe previous outputs were: ")
    output = backtrack('1010101100001001')
    for i in range(4):
        output = backtrack(output)
    print("\nWe can generate the next 5 outputs through using the processarray function, so we will use that.")
    processedArray = processArray('1010101100001001')
    for i in range(5):
        print("The next value is: {}".format(processedArray))
        processedArray = processArray(processedArray)
    print("We can generate the next 5, so there is no backtracking or prediction resistance.")
main()

#NOTE: The PRNG in part C is not cryptographically secure because we can backtrack based on the PRNG implementation. 
# Because the first bits gives us the mod 2 of the 11,13,14 and 16 bit, then mod 2 of the 1, 12, 14 and 15 bit of the
# output gives us what the previous 16 bit was. And of course since we implemented the processing array that is used for
# the prng, we can similarly generate the next 5