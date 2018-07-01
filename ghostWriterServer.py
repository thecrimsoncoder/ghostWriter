#!/usr/bin/env python3

from flask import Flask
from threading import Thread
import json, random, sys, time, hashlib

app = Flask(__name__)

@app.route('/OTR/api/v1.0/otr/<string:api_key>',methods=['GET'])
def get_otr(api_key):
    if auth_api_key(api_key) == True:
        OTR = create_one_time_rotor_setting()
        return OTR
    else:
        response = {"Status": "Invalid API Key"}
        return json.dumps(response)

@app.route('/OTR/api/v1.0/otr/<string:api_key>/<string:rotor_setting>/<string:message_hash>',methods=['POST'])
def put_otr(api_key,rotor_setting,message_hash):
    if auth_api_key(api_key) == True:
        key_value = {message_hash : rotor_setting}
        try:
            with open("ghostWriterServerMessageDatabase.json", "r") as json_database:
                database = json.load(json_database)
                database["message_database"].append(key_value)
            with open("ghostWriterServerMessageDatabase.json", "w") as json_database:
                json.dump(database,json_database, indent=4, separators=(',', ' : '))
            response = {"Status": "Message Successfully Generated"}
            return json.dumps(response)
        except Exception as e:
            print(e)
            response = {"Status": "Invalid Token"}
            return json.dumps(response)
    else:
        response = {"Status": "Invalid API Key"}
        return json.dumps(response)

@app.route('/OTR/api/v1.0/otr/<string:api_key>/<string:message_hash>', methods=['GET'])
def auth_otr(api_key,message_hash):
    if auth_api_key(api_key) == True:
        try:
            with open("ghostWriterServerMessageDatabase.json", "r") as json_database:
                database = json.load(json_database)
                database = database["message_database"]
                for message in database:
                    if str(list(dict(message).keys())[0]) == str(message_hash):
                        rotor_setting = dict(message).get(str(message_hash))
                        rotor_setting = parseRotorSetting(rotor_setting)
                        return json.dumps(rotor_setting)
        except Exception as e:
            print(e)
            response = {"Status": "Database Error"}
            return json.dumps(response)
    else:
        response = {"Status": "Invalid API Key"}
        return json.dumps(response)

def auth_api_key(api_key):
    try:
        with open("ghostWriterServerAPIDatabase.json","r") as api_database:
            database = json.loads(api_database.read())
            database = database["api_database"]

            for key in database:
                if dict(key).get(api_key) == True:
                    return True

    except Exception as e:
        print(e)
        return False

def create_api_key():

    api_key = str(hashlib.md5(str(time.time()).encode('utf-8')).hexdigest())
    key_value = {api_key : True}

    try:
        with open("ghostWriterServerAPIDatabase.json" ,"r") as json_database:
            database = json.loads(json_database.read())
            database["api_database"].append(key_value)
        with open("ghostWriterServerAPIDatabase.json", "w") as json_database:
            json.dump(database,json_database, indent=4, separators=(',', ' : '))
        return api_key
    except Exception as e:
        print(e)
        response = {"Status": "API Database Error"}
        return json.dumps(response)

def import_settings():
    try:
        with open("ghostWriterServerSettings.json", "r") as json_config:
            server_config = json.load(json_config)
        PORT = server_config["port"]
        HOST = server_config["host"]
        return HOST, PORT
    except Exception as e:
        print(e)
        return False

def parseRotorSetting(rotor_setting):
    keys = list()
    values = rotor_setting.split("|")
    for x in range(0,len(values)):
        keys.append(int(x))
    rotor_setting_json = dict(zip(keys,values))
    return rotor_setting_json

def create_one_time_rotor_setting():
    rotor_key = []
    rotor_value = []
    for rotor_num in range(0,3):
        rotor_key.append(rotor_num)
        rotor_value.append(random.randint(1,9999))
    rotor_config = dict(zip(rotor_key,rotor_value))
    rotor_config = json.dumps(rotor_config)
    return rotor_config

def flask_app():
    app.run(port=PORT,debug=False)

def server_title():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+     g h o s t W r i t e r S e r v e r . p y      +")
    print("+            Created By: Sean McElhare             +")
    print("+            github.com/thecrimsoncoder            +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

def server_menu():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+  1. Run the server                               +")
    print("+  2. Create Client API Key                        +")
    print("+  3. Quit because you are a quitter!              +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
    option = int(input("Just tell me what you want, what you really really want!: "))

    if int(option) == 1:
        flask_server = Thread(target=flask_app())
        flask_server.start()
        server_menu()
    elif int(option) == 2:
        new_api_key = create_api_key()
        new_api_json = json.dumps({new_api_key : str(HOST)+":"+str(PORT)})
        print("API Key: " + str(new_api_json))
        print("Copy and give this key to a trusted client, you can revoke access by setting " + new_api_key + " to 'False' later in ghostWriterServerAPIDatabase.json.")
        server_menu()
    elif int(option) == 3:
        print("RmFyZXdlbGwgVHJhdmVsZXIgLVRoZUNyaW1zb25Db2Rlcg==")
        sys.exit(0)
    else:
        print("Ummmm you need to pick a valid option")
        time.sleep(2)
        server_menu()

if __name__ == "__main__":
    HOST, PORT  = import_settings()
    server_title()
    server_menu = Thread(target=server_menu())
    server_menu.start()