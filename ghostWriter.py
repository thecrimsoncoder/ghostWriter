
import logging
import sys
import time

def main():
    programTitle()
    if(checkSetup() == True):
        option = menu()
        if(option == 1):
            createMessage()
        elif(option == 2):
            createDBToken()
        elif(option == 3):
            decodeMessage()
        elif(option == 4):
            print("01100011011000010111001001110000011001010010000001100100011010010110010101101101")
            sys.exit(0)
        else:
            print("Ummmm you need to pick a valid option")
            time.sleep(2)
            menu()

def createMessage():
    return True
def createDBToken():
    return True
def decodeMessage():
    return True
def checkSetup():
    return True


def programTitle():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+     g h o s t W r i t e r . p y      +")
    print("+     Created By: TheCrimsonCoder      +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return True

def menu():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+  1. Create a new message             +")
    print("+  2. Create a DB token                +")
    print("+  3. Decode message                   +")
    print("+  4. Quit because you are a quitter!  +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return int(input("Watcha wanna do?: "))

main()