#!/usr/bin/env python3
import sys, time, base64, requests, json
from _rotor import _rotor

def main():
    programTitle()
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
    ROTORS = list()
    HOST, PORT = import_settings()
    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr"
    rotor_setting = requests.get(request)
    rotor_setting_json = rotor_setting.json()

    for x in range(0,3):
        new_rotor = _rotor()
        new_rotor.configureRotor(rotor_setting_json[str(x)])
        ROTORS.append(new_rotor)

    print(ROTORS)
def stepRotor(_rotor):
    return _rotor.configureRotor(1)

    # message = input("Message: ")
    #
    # # TESTING ONLY, really because i only defined the dictionary to have upper case letters
    # message.upper()

def decodeMessage(encodedMessage):
    print(base64.b64decode(encodedMessage))

def import_settings():
    try:
        with open("ghostWriterSettings.json") as json_config:
            client_config = json.load(json_config)
        PORT = client_config["port"]
        HOST = client_config["host"]
        return HOST,PORT
    except:
        FileNotFoundError()
        return False


def programTitle():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+     g h o s t W r i t e r . p y      +")
    print("+     Created By: TheCrimsonCoder      +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")

def menu():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+  1. Create a new message             +")
    print("+  2. Decode message                   +")
    print("+  3. Quit because you are a quitter!  +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return int(input("Just tell me what you want, what you really really want!: "))

main()