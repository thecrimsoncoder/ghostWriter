#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
import json
import random

APPLICATION = Flask(__name__)
API = Api(APPLICATION)

class OTR(Resource):
    def get(self):
        OTR = create_one_time_rotor_setting()
        return OTR

    def put(self,rotor_setting,message_hash):
        return rotor_setting,message_hash

class Auth_OTR(Resource):
    def get(self, message_hash):
        return message_hash

def import_settings():
    with open("ghostWriterServerSettings.json") as json_config:
        server_config = json.load(json_config)
    PORT = server_config["port"]
    return PORT

def create_one_time_rotor_setting():
    OTR = ""
    for rotor in range(1,3):
        OTR = OTR + str(random.randint(1,5000))
    print(OTR)
    return OTR

if __name__ == "__main__":
    PORT = import_settings()
    APPLICATION.run(port=PORT)

API.add_resource(OTR,'/OTR')
API.add_resource(OTR,'/OTR/<rotor_setting>/<message_hash>')
API.add_resource(Auth_OTR,'/Auth/<message_hash>')


