"""
Author: Robert Elsom
Date: 4/19/2019
Description: Creates an Enigma Machine that creates a cipher text based on the Enigma
Machine used by Germany during World War 2, but each disk is a simple Ceasar cipher that
rotates like the original Enigma Machine. There is also one rewire to represent the plug board element

"""
import Enigma_Encryption
import Enigma_Decryption

#encrypts a sentence
def encryptSentence(sentence):
    string = Enigma_Encryption.encrypt(sentence)
    return string

#decrypts a sentence
def decryptSentence(sentence):
    string = Enigma_Decryption.decrypt(sentence)
    return string

#encrypts a file
def encryptFile(fileName):
    try:
        textFile = open(fileName, "r")
        text = textFile.read()
        output = open(fileName[:-4] + "_cipher_text.txt", "a")
        encryption = Enigma_Encryption.encrypt(str(text[0:len(text)]))
        output.write(encryption[0])
        print("Encrypted Text is written to " + fileName[:-4] + "_cipher_text.txt")
        print("The key to decrypt is " + str(encryption[1])) 
        textFile.close()
        output.close()
        cipherFile = fileName[:-4] + "_cipher_text.txt"
    except:
        print("Invalid File Name")
        exit(0)

#decrypts a file
def decryptFile(fileName):
    try:
        textFile = open(fileName, "r")
        text = textFile.read()
        output = open(fileName[:-16] + "_decrypted_text.txt", "a")
        output.write(Enigma_Decryption.decrypt(text[0:len(text)]))
        print("Encrypted Text is written to " + fileName[:-16] + "_decrypted_text.txt")
    except:
        print("Invalid File Name")
        exit(0)

# Appends .txt to end of file name if not present
def appendExtension(fileName):
    if ".txt" != fileName[-4:]:
        return '.txt'

    return ''


# gets file name from user, calls appendExtension, then calls openFile
def inputFilePath():
    prompt = ("Enter the file path to the txt file you would like to encrypt\n")
    filePath = input(prompt)
    filePath += appendExtension(filePath)

    return filePath

#gets user inputted string
def inputString():
    sentence = input("Enter a sentence to encrypt\n")

    return sentence


#validates user input is a valid choice
def validateChoice(userChoice):
    while (int(userChoice) < 1 or int(userChoice) > 4):
        userChoice = input("Sorry, that is not a valid input. Please try again\n")

    return userChoice

#converts choice to a string for function call
def convertUserChoice(userChoice):
    if userChoice == '1':
        userChoice = 'e.sentence'
    elif userChoice == '3':
        userChoice = 'e.txt file'
    elif userChoice == '2':
        userChoice = 'd.sentence'
    else:
        userChoice = 'd.txt file'


    return userChoice

#start menu for user to choose what action they want to perform
def chooseAction():
    prompt = ("Choose one fo the following:\n"
              "\t1. Encrypt a sentence in the console\n"
              "\t2. Decrypt a sentence in the console\n"
              "\t3. Encrypt a text file and output to <filename>_cipher_text.txt\n"
              "\t4. Decrypt a text file and output to <filename>_decrypted_text.txt\n\n")

    userChoice = input(prompt)
    userChoice = validateChoice(userChoice)
    userChoice = convertUserChoice(userChoice)
	
    return userChoice

#prints instructions then makes function calls based on user input
def main():
    print("\nWelcome to the Enigma Encryption Machine!\n"
          "We use a simple Ceasar cipher to represent each scrambler, \n"\
          "and a simple letter swap to represent the plug board. \n"\
          "The offsets are rotated after each letter like the original Enigma\n"\
          "machines scramblers. You have the option to set the\n" \
          "Ceasar keys, encrypt and decrypt files in the console, \n"\
          "or encrypt and decrypt entire txt files\n\n")
    userChoice = chooseAction()
    if userChoice == 'e.sentence':
        sentence = inputString()
        cipherText = encryptSentence(sentence)
        print("Encrypted Text: " + cipherText[0])
        print("Key: " + str(cipherText[1]))
    elif userChoice == 'd.sentence':
        sentence = inputString()
        plainText = decryptSentence(sentence)
        print("Plain Text: " + plainText)
    elif userChoice == 'e.txt file':
        filePath = inputFilePath()
        encryptFile(filePath)
    else:
        filePath = inputFilePath()
        decryptFile(filePath)



if __name__ == "__main__":
    main()
