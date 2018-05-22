#!/usr/bin/env python3
from flask import Flask
import json, random

app = Flask(__name__)

@app.route('/OTR/api/v1.0/otr',methods=['GET'])
def get_otr():
    OTR = create_one_time_rotor_setting()
    return OTR

@app.route('/OTR/api/v1.0/otr/<string:rotor_setting>/<string:message_hash>',methods=['POST'])
def put_otr(rotor_setting,message_hash):
    key_value = {rotor_setting : message_hash}
    try:
        with open("ghostWriterDatabase.json") as json_database:
            database = json.load(json_database)
        database.update(key_value)
        with open("ghostWriterDatabase.json", "w") as json_database:
            json.dump(database,json_database)
        response = {"Status": "Message Successfully Generated"}
        return json.dumps(response)
    except:
        FileNotFoundError()
        response = {"Status": "Database Error"}
        return json.dumps(response)

@app.route('/OTR/api/v1.0/otr/<string:message_hash>', methods=['GET'])
def auth_otr(message_hash):
    try:
        with open("ghostWriterDatabase.json") as json_database:
            database = json.load(json_database)
        rotor_setting = parseRotorSetting(list(database.keys())[list(database.values()).index(str(message_hash))])
        return json.dumps(rotor_setting)
    except:
        FileNotFoundError()
        response = {"Status": "Database Error"}
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
    rotor = dict(zip(rotor_key,rotor_value))
    rotor = json.dumps(rotor)
    return rotor

if __name__ == "__main__":
    PORT = import_settings()
    app.run(port=PORT)


