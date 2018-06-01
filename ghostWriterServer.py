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
        key_value = {rotor_setting : message_hash}
        try:
            with open("ghostWriterDatabase.json") as json_database:
                database = json.load(json_database)
            database.update(key_value)
            with open("ghostWriterDatabase.json", "w") as json_database:
                json.dump(database,json_database, indent=4, separators=(',', ': '))
            response = {"Status": "Message Successfully Generated"}
            return json.dumps(response)
        except:
            FileNotFoundError()
            response = {"Status": "Invalid Token"}
            return json.dumps(response)
    else:
        response = {"Status": "Invalid API Key"}
        return json.dumps(response)

@app.route('/OTR/api/v1.0/otr/<string:api_key>/<string:message_hash>', methods=['GET'])
def auth_otr(api_key,message_hash):
    if auth_api_key(api_key) == True:
        try:
            with open("ghostWriterDatabase.json") as json_database:
                database = json.load(json_database)
            rotor_setting = parseRotorSetting(list(database.keys())[list(database.values()).index(str(message_hash))])
            return json.dumps(rotor_setting)
        except:
            FileNotFoundError()
            response = {"Status": "Database Error"}
            return json.dumps(response)
    else:
        response = {"Status": "Invalid API Key"}
        return json.dumps(response)

def auth_api_key(api_key):
    try:
        with open("ghostWriterAPIDatabase.json") as json_api_database:
            api_database = json.load(json_api_database)
            if api_database[api_key] == True:
                return True
            else:
                return False
    except:
        FileNotFoundError()
        response = {"Status": "API Database Error"}
        return json.dumps(response)

def create_api_key():

    api_key =  hashlib.md5(time.time()).encode('utf-8').hexdigest()
    key_value = {api_key : True}
    try:
        with open("ghostWriterAPIDatabase.json") as json_database:
            database = json.load(json_database)
        database.update(key_value)
        with open("ghostWriterAPIDatabase.json", "w") as json_database:
            json.dump(database,json_database, indent=4, separators=(',', ': '))
        return True
    except:
        FileNotFoundError()
        response = {"Status": "API Database Error"}
        return json.dumps(response)

def import_settings():
    try:
        with open("ghostWriterServerSettings.json") as json_config:
            server_config = json.load(json_config)
        PORT = server_config["port"]
        return PORT
    except:
        FileNotFoundError()
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
    PORT = import_settings()
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
        create_api_key()
        server_menu()
    elif int(option) == 3:
        print("RmFyZXdlbGwgVHJhdmVsZXIgLVRoZUNyaW1zb25Db2Rlcg==")
        sys.exit(0)
    else:
        print("Ummmm you need to pick a valid option")
        time.sleep(2)
        server_menu()

if __name__ == "__main__":
    server_title()
    server_menu = Thread(target=server_menu())
    server_menu.start()

#Li4uLnlvdSByZWFsbHkgaHVydCBtZSBiYWQsIHlvdXIgYWN0aW9ucyBhcmUgdW5mb3JnaXZhYmxlLiBZb3UgYXJlIG5vIGxvbmdlciBhIGxvdmVyIG9mIG1pbmUgc28gc3RvcCBhc2tpbmcgdG8gYmUgZnJpZW5kcy4=