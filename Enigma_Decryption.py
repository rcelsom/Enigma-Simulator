"""
Author: Robert Elsom
Date: 4/19/2019
Description: Recieves a sentence or file name and decrypts the sentence or entire
file according the same way an Enigma machine would work using the same key it was encrypted with

"""

import Enigma_Settings
# decrypts string by cycling through the enigma machine in reverse
def decrypt(string):
    count = 0
    plainText = ''
    key = [0,0,0,'a','b']
    key = Enigma_Settings.setKey()

    cylinder1Shift = int(key[0])
    cylinder2Shift = int(key[1])
    cylinder3Shift = int(key[2])
    plugBoardSettings = [key[3], key[4]]

    for letter in string:
        # gets letters, if not letter just ignores it
        if (letter.isalpha()):
            # checks if letter is switched in plugboard
            if (letter == plugBoardSettings[0]):
                letter = plugBoardSettings[1]
            elif (letter == plugBoardSettings[1]):
                letter = plugBoardSettings[0]
            letter = letter.lower()
            letter = cylinder1(letter, cylinder1Shift)
            letter = cylinder2(letter, cylinder2Shift)
            letter = cylinder3(letter, cylinder3Shift)
            letter = reflect(letter)
            letter = cylinder3(letter, cylinder3Shift)
            letter = cylinder2(letter, cylinder2Shift)
            letter = cylinder1(letter, cylinder1Shift)
            if letter == plugBoardSettings[1]:
                letter = plugBoardSettings[0]
            elif letter == plugBoardSettings[0]:
                letter = plugBoardSettings[1]

            count += 1
            #changes ceasar shift on the three cylinders
            cylinder1Shift = rotate(cylinder1Shift);

            # rotates cylinder 2 every time cylinder 1 completes a rotation
            if(count % 26 == 0):
                cylinder2Shift = rotate(cylinder2Shift)
            # rotates cylinder 3 every time cylinder 2 completes a rotation
            elif (count % 676 == 0):
                cylinder3Shift = rotate(cylinder3Shift)

            plainText += letter
        #keeps spaces and newline characters to keep readability
        elif (letter == '\n' or letter == ' '):
            plainText += letter

    return plainText





#crotates the disk
def rotate(currentOffset):
    if (currentOffset < 26):
        return (currentOffset+1)
    else:
        return 1

#kept as three functions to symbollicly represent the three disk
# rather than simplifying into a singe function.
def cylinder1(char, shift):
    if (ord(char) - int(shift) >= 97):
        return chr(ord(char) - shift)
    else:
        return chr(ord(char) + (26 - shift))
    return char

def cylinder2(char, shift):
    if (ord(char) - int(shift) >= 97):
        return chr(ord(char) - shift)
    else:
        return chr(ord(char) + (26 - shift))
    return char

def cylinder3(char, shift):
    if (ord(char) - int(shift) >= 97):
        return chr(ord(char) - shift)
    else:
        return chr(ord(char) + (26 - shift))
    return char

#represents the mirror at the end of the enigma machine, has a constant shift of 5
def reflect(char):
    if (ord(char) - 5 >= 97):
        return chr(ord(char) - 5)
    else:
        return chr(ord(char) + 21)


