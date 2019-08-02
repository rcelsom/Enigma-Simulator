"""
Author: Robert Elsom
Date: 4/19/2019
Description: Recieves a sentence or file name and encrypts the sentence or entire
file according the same way an Enigma machine would work

"""
import Enigma_Settings

def encrypt(string):
    count = 0
    cipherText = ''
    #sets settings for the encryption
    cylinder1Shift = Enigma_Settings.setCylinder1()
    cylinder2Shift = Enigma_Settings.setCylinder2()
    cylinder3Shift = Enigma_Settings.setCylinder3()
    plugBoardSettings = Enigma_Settings.setPlugBoard()
    key = [cylinder1Shift, cylinder2Shift, cylinder3Shift, plugBoardSettings[0],            
           plugBoardSettings[1]]

    for letter in string:
        # gets letters, if not letter just ignores it
        if (letter.isalpha()):
            letter = letter.lower()
            # checks if letter is switched in plugboard
            if letter == plugBoardSettings[0]:
                letter = plugBoardSettings[1]
            elif letter == plugBoardSettings[1]:
                letter = plugBoardSettings[0]
            letter = cylinder1(letter, cylinder1Shift)
            letter = cylinder2(letter, cylinder2Shift)
            letter = cylinder3(letter, cylinder3Shift)
            letter = reflect(letter)
            letter = cylinder3(letter, cylinder3Shift)
            letter = cylinder2(letter, cylinder2Shift)
            letter = cylinder1(letter, cylinder1Shift)
            if letter == plugBoardSettings[0]:
                letter = plugBoardSettings[1]
            elif letter == plugBoardSettings[1]:
                letter = plugBoardSettings[0]

            count += 1
            #changes ceasar shift on the three cylinders
            cylinder1Shift = rotate(cylinder1Shift);

            # rotates cylinder 2 every time cylinder 1 completes a rotation
            if(count % 26 == 0):
                cylinder2Shift = rotate(cylinder2Shift)
            # rotates cylinder 3 every time cylinder 2 completes a rotation
            elif (count % 676 == 0):
                cylinder3Shift = rotate(cylinder3Shift)

            cipherText += letter
        elif (letter == '\n' or letter == ' '):
            cipherText += letter

    return cipherText, key





#crotates the disk
def rotate(currentOffset):
    if (currentOffset < 26):
        return (currentOffset+1)
    else:
        return 1

#kept as three functions to symbollicly represent the three disk
# rather than simplifying into a singe function.
def cylinder1(char, shift):
    if (ord(char) + int(shift) <= 122):
        return chr(ord(char) + shift)
    else:
        return chr(ord(char) - (26 - shift))
    return char

def cylinder2(char, shift):
    if (ord(char) + shift <= 122):
        return chr(ord(char) + shift)
    else:
        return chr(ord(char) - (26 - shift))
    return char

def cylinder3(char, shift):
    if (ord(char) + shift <= 122):
        return chr(ord(char) + shift)
    else:
        return chr(ord(char) - (26 - shift))
    return char

#represents the mirror at the end of the enigma machine, has a constant shift of 5
def reflect(char):
    if (ord(char) + 5 <= 122):
        return chr(ord(char) + 5)
    else:
        return chr(ord(char) - 21)






