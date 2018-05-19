
import logging
import sys

def main():
    programTitle()
    if(checkSetup == True):
       if(menu() == 1):
           createMessage()
       elif(menu() == 2):
           createDBToken()
       elif(menu() == 3):
           decodeMessage()
       elif(menu() == 4):
           sys.exit(0)




def checkSetup(se):
    return True

def programTitle():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+     g h o s t W r i t e r . p y      +")
    print("+     Created By: TheCrimsonCoder      +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")

def menu():

main()