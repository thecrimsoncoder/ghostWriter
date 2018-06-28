#!/usr/bin/env python3
import sys, time, requests, json, hashlib
from _rotor import rotor


def main():

    option = menu()
    if(int(option) == 1):
        contact_server(encodeMessage(promptInput()))
        main()
    elif(int(option) == 2):
        decodeMessage(promptInput())
        main()
    elif(int(option) == 3):
        importAPIKey()
        main()
    elif(int(option) == 4):
        selectActiveServer()
        main()
    elif(int(option) == 5):
        print("Q2FycGUgRGllbSEgLVRoZUNyaW1zb25Db2Rlcg==")
        sys.exit(0)
    else:
        print("Ummmm you need to pick a valid option")
        time.sleep(2)
        main()

def promptInput():
    message = input("Message: ")
    return message

def encodeMessage(cleartext):

    ROTORS = list()
    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr"
    rotor_setting = requests.get(request)
    rotor_setting_json = rotor_setting.json()
    cipher_text = ""
    rotor0Itererator = 0
    rotor1Itererator = 0
    return_list = list()
    ROTOR_COUNT = 3

    for x in range(0, ROTOR_COUNT):
        new_rotor = rotor()
        new_rotor.configureEncoderRotor(rotor_setting_json[str(x)])
        ROTORS.append(new_rotor)

    cleartext_array = list(cleartext)

    for char in cleartext_array:
        cipher_text = cipher_text + ROTORS[2].mapping[ROTORS[1].mapping[ROTORS[0].mapping[char]]]
        ROTORS[0].rotorStepForward()
        rotor0Itererator += 1
        if(rotor0Itererator == len(ROTORS[0].mapping)):
            ROTORS[1].rotorStepForward()
            rotor0Itererator = 0
            rotor1Itererator += 1
        if(rotor1Itererator == len(ROTORS[1].mapping)):
            ROTORS[2].rotorStepForward()
            rotor1Itererator = 0

    cipher_text_hash = hashlib.md5(str(cipher_text).encode('utf-8')).hexdigest()

    print("\n==============================================================================================\n")
    print("Cipher Text (COPY THIS AND SEND TO RECIPIENT): \n" + cipher_text)
    print("\n==============================================================================================\n")
    print("Cipher Hash: " + cipher_text_hash)
    print("\n==============================================================================================\n")

    return_list.append(rotor_setting_json)
    return_list.append(cipher_text_hash)

    return return_list

def contact_server(arg_list):
    rotor_setting = ""
    rotor_setting_json = arg_list[0]
    cipher_text_hash = arg_list[1]
    ROTOR_COUNT = 3

    for x in range(0, ROTOR_COUNT):
        rotor_setting = rotor_setting + str(rotor_setting_json[str(x)]) + "|"

    rotor_setting_list = list(rotor_setting)
    del rotor_setting_list[len(rotor_setting_list)-1]
    rotor_setting_string = ''.join(rotor_setting_list)

    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr/" + rotor_setting_string + "/" + cipher_text_hash
    requests.post(request)

def decodeMessage(encodedMessage):
    clearText = ""
    rotor0Itererator = 0
    rotor1Itererator = 0
    ROTORS = list()
    request = "http://" + str(HOST) + ":" + str(PORT) + "/OTR/api/v1.0/otr/" + hashlib.md5(str(encodedMessage).encode('utf-8')).hexdigest()
    rotor_setting = requests.get(request)
    rotor_setting_json = rotor_setting.json()
    ROTOR_COUNT = 3

    for x in range(0, ROTOR_COUNT):
        new_rotor = rotor()
        new_rotor.configureDecoderRotor(int(rotor_setting_json[str(x)]))
        ROTORS.append(new_rotor)

    encodedText = list(encodedMessage)

    for char in encodedText:
        clearText = clearText + str(ROTORS[0].mapping[ROTORS[1].mapping[ROTORS[2].mapping[str(char)]]])
        ROTORS[0].rotorStepBackward()
        rotor0Itererator += 1
        if(rotor0Itererator == len(ROTORS[0].mapping)):
            ROTORS[1].rotorStepBackward()
            rotor0Itererator = 0
            rotor1Itererator += 1
        if(rotor1Itererator == len(ROTORS[1].mapping)):
            ROTORS[2].rotorStepBackward()
            rotor1Itererator = 0

    print("\n==============================================================================================\n")
    print("Decoded Message: " + clearText)
    print("\n==============================================================================================\n")
def selectActiveServer():
    option_number = 1
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+           API Server List            +")
    print("++++++++++++++++++++++++++++++++++++++++")
    try:
        with open("ghostWriterAPIDatabase.json", "r") as api_database:
            database = json.loads(api_database.read())
            option_list = database["api_database"]
            for host in option_list:
                print(str(option_number)+". " + str(list(dict(host).keys())[0]))
                print(host["active"])
                option_number += 1
            option  = int(input("Enter the number of the Server you wish to activate for encoding/decoding"))

            # Cycle through and set all servers to false
            # Set line item to true
    except Exception as e:
        print(e)
        return False
def importAPIKey():
    api_key_input = str(input("Paste API Key Here: "))
    api_key_input = json.loads(api_key_input)

    API_KEY = list(dict.keys(api_key_input))[0]

    api_key_input_values = list(dict.values(api_key_input))
    api_key_input_values = str(api_key_input_values[0]).split(":")

    API_HOST = api_key_input_values[0]
    API_PORT = api_key_input_values[1]
    API_ACTIVE = False

    import_key = {
        str(API_HOST) : {
            "port" : int(API_PORT),
            "api_key" : str(API_KEY),
            "active" : API_ACTIVE
        }
    }

    try:
        with open("ghostWriterAPIDatabase.json", "r") as api_database:
             api_json_database = json.loads(api_database.read())
             api_json_database["api_database"].append(import_key)
        with open("ghostWriterAPIDatabase.json", "w") as api_database:
            json.dump(api_json_database, api_database, indent=4, separators=(',', ' : '))
            return True
    except Exception as e:
        print(e)
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
    print("+  3. Import API Key                   +")
    print("+  4. Select Active Server             +")
    print("+  5. Quit because you are a quitter!  +")
    print("++++++++++++++++++++++++++++++++++++++++")

    return int(input("Just tell me what you want, what you really really want!: "))

programTitle()
main()