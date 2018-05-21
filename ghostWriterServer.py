#!/usr/bin/env python3
from flask import Flask
import jsonify
import json
import random

app = Flask(__name__)

@app.route('/OTR/api/v1.0/otr',methods=['GET'])
def get_otr():
    OTR = create_one_time_rotor_setting()
    return OTR

@app.route('/OTR/api/v1.0/otr/<string:rotor_setting>/<string:message_hash>',methods=['GET'])
def put_otr(rotor_setting,message_hash):
    return rotor_setting,message_hash

@app.route('/OTR/api/v1.0/otr/<string:message_hash>', methods=['GET'])
def auth_otr(message_hash):
    return message_hash

def import_settings():
    with open("ghostWriterServerSettings.json") as json_config:
        server_config = json.load(json_config)
    PORT = server_config["port"]
    return PORT

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
    app.run(port=PORT, debug=True)


