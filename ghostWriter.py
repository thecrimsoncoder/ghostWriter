import sys
import time
import base64
import _rotor

def main():
    programTitle()
    if(checkSetup() == True):
        option = menu()
        if(option == 1):
            createMessage()
        elif(option == 2):
            decodeMessage(str(input("Copy and Paste the encoded message here")))
        elif(option == 3):
            print("01100011011000010111001001110000011001010010000001100100011010010110010101101101")
            sys.exit(0)
        else:
            print("Ummmm you need to pick a valid option")
            time.sleep(2)
            menu()

def createMessage():
    return True
def decodeMessage(encodedMessage):
    print(base64.b64decode(encodedMessage))
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
    print("+  2. Decode message                   +")
    print("+  3. Quit because you are a quitter!  +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return int(input("Just tell me what you want, what you really really want!: "))

main()