#!/usr/bin/env python3
import sys, time, requests, json, hashlib
from _rotor import _rotor


def main():

    option = menu()
    if(option == 1):
        contact_server(encodeMessage(createMessage()))
    elif(option == 2):
        decodeMessage(createMessage())
    elif(option == 3):
        print("Q2FycGUgRGllbSEgLVRoZUNyaW1zb25Db2Rlcg==")
        sys.exit(0)
    else:
        print("Ummmm you need to pick a valid option")
        time.sleep(2)
        main()

def createMessage():
    message = input("Message: ")
    return message

def encodeMessage(cleartext):

    ROTORS = list()
    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr"
    rotor_setting = requests.get(request)
    rotor_setting_json = rotor_setting.json()
    cipher_text = ""
    return_list = list()

    for x in range(0, ROTOR_COUNT):
        new_rotor = _rotor()
        new_rotor.configureRotor(rotor_setting_json[str(x)])
        ROTORS.append(new_rotor)

    cleartext_array = list(cleartext)

    for char in cleartext_array:
        cipher_text = cipher_text + ROTORS[2].mapping[ROTORS[1].mapping[ROTORS[0].mapping[char]]]
        ROTORS[0].configureRotor(1)

    print("\n==============================================================================================\n")
    print("Cipher Text (COPY THIS AND SEND TO RECIPIENT): " + cipher_text)
    print("\n==============================================================================================\n")
    cipher_text_hash = hashlib.md5(str(cipher_text).encode('utf-8')).hexdigest()
    print("Cipher Hash: " + cipher_text_hash)
    print("\n==============================================================================================\n")

    return_list.append(rotor_setting_json)
    return_list.append(cipher_text_hash)

    return return_list

def contact_server(arg_list):
    rotor_setting = ""
    rotor_setting_json = arg_list[0]
    cipher_text_hash = arg_list[1]

    for x in range(0, ROTOR_COUNT):
        rotor_setting = rotor_setting + str(rotor_setting_json[str(x)]) + "|"

    rotor_setting_list = list(rotor_setting)
    del rotor_setting_list[len(rotor_setting_list)-1]
    rotor_setting_string = ''.join(rotor_setting_list)

    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr/" + rotor_setting_string + "/" + cipher_text_hash
    requests.post(request)


def decodeMessage(encodedMessage):
    ROTORS = list()
    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr/" + hashlib.md5(str(encodedMessage).encode('utf-8')).hexdigest()
    rotor_setting = requests.get(request)
    rotor_setting_json = rotor_setting.json()

    for x in range(0, ROTOR_COUNT):
        new_rotor = _rotor()
        new_rotor.configureRotor(int(rotor_setting_json[str(x)]))
        ROTORS.append(new_rotor)

    for x in ROTORS:
        print(x.mapping)
    return True

def import_settings():
    try:
        with open("ghostWriterSettings.json") as json_config:
            client_config = json.load(json_config)
        PORT = client_config["port"]
        HOST = client_config["host"]
        ROTOR_COUNT = client_config["rotor_count"]
        return HOST,PORT,ROTOR_COUNT
    except:
        FileNotFoundError()
        return False


def programTitle():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+     g h o s t W r i t e r . p y      +")
    print("+     Created By: Sean McElhare        +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")

def menu():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+  1. Create a new message             +")
    print("+  2. Decode message                   +")
    print("+  3. Quit because you are a quitter!  +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return int(input("Just tell me what you want, what you really really want!: "))

HOST, PORT, ROTOR_COUNT = import_settings()
programTitle()
main()
