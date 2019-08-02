"""
Author: Robert Elsom
Date: 4/19/2019
Description: Called to set the setting of the enigma machine, from swapping wires
to setting the scramblers
"""
# sets offset for cylinder1
def setCylinder1():
    cylinder1 = int(input("What ceasar shift would you like to start cylinder 1 on? [1...26]\n"))
    while (cylinder1 < 1 or cylinder1 > 26):
        cylinder1 = int(input("\nSorry, that is not in the range [1...26]"))
    return cylinder1

#sets offset for cylinder 2
def setCylinder2():
    cylinder2 = int(input("What ceasar shift would you like to start cylinder 2  on? [1...26]\n"))
    while (cylinder2< 1 or cylinder2> 26):
        cylinder2= int(input("\nSorry, that is not in the range [1...26]"))
    return cylinder2

# sets offset for cylinder 3
def setCylinder3():
    cylinder3 = int(input("What ceasar shift would you like to start cylinder 3 on? [1...26]\n"))
    while (cylinder3 < 1 or cylinder3 > 26):
        cylinder3 = int(input("\nSorry, that is not in the range [1...26]"))
    return cylinder3

# sets the letters to swap to represent changing the wiring
def setPlugBoard():
    firstLetter = input("What is the first letter you would like to swap?\n")
    while (not firstLetter.isalpha() or len(firstLetter) > 1):
        firstLetter = input("Sorry, the first letter must be a single letter.\n")

    secondLetter = input("What letter would you like to swap " + firstLetter + ' with?\n')

    while(not secondLetter.isalpha() or len(secondLetter) > 1):
        secondLetter = input("Sorry, the second letter must be a single letter.\n")

    while (firstLetter == secondLetter):
        secondLetter = input("Sorry, the second letter cannot be the same as the first."\
        " Please enter another one.\n")
    return [firstLetter.lower(), secondLetter.lower()]

# sets the key for decryption
def setKey():
    key = input("What is the key to decrypt? \n"\
          "Enter each symbol seperated by a comma with no spaces\n")
    keyArr = key.split(',')
    return keyArr
