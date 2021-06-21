#Raphael Dela Cruz 2/26/21

#Method that runs all functions. NOTE: This program does not count letters if they do not appear, in my file the letter "z" does not appear so it does not show that it appears 0 times.
def main():
    #Remember to include file type. For example, to read a txt file called lorem, do lorem.txt
    userInput = input("Enter the file name you would like to read: ")
    countDictionary = countLetter(getText(userInput))
    for k,v in countDictionary.items():
        print("The letter {} appears {} times.".format(k, v))


#Function that counts letters in a sentence (or in this case, a file of text), then returns a list
def countLetter(sentence):
    #Create empty dictionary
    dictionary = {}
    #Iterates through each letter, checks if it is a letter in the alphabet and adds it to dictionary
    for i in sentence:
        if(i.isalpha()):
            dictionary[i.lower()] = dictionary.get(i.lower(),0) + 1
    #Sorts the dictionary so that the number of occurences for a is the very first key value.
    sortedDict = sorted(dictionary.items())
    return dict(sortedDict)

#Opens text file to obtain string value, then returns the string.
def getText(fileName):
    fileOpen = open(fileName)
    return fileOpen.read()

main()