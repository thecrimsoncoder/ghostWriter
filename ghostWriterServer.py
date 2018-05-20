#!/usr/bin/env python3

import json
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import random
import time



def import_settings():
    with open("ghostWriterServerSettings.json") as json_config:
        server_config = json.load(json_config)

    HOST = server_config["host"]
    PORT = server_config["port"]
    BUFFER_SIZE = server_config["buffer_size"]
    ONE_TIME_ROTOR_SETTING = server_config["one_time_rotor_setting_timeout"]

    return HOST,PORT,BUFFER_SIZE,ONE_TIME_ROTOR_SETTING


def accept_incomming_connection():
        client, client_address = SERVER.accept()
        Thread(target=client_request, args=(client,)).start()
        Thread(target=create_one_time_rotor_setting()).start()

def client_request(client):
    message = client.recv(BUFFER_SIZE)

    if(message.bytes("ZXhjdXNlIG1lLCBtYXkgSSBoYXZlIGEgdG9rZW4gcGxlYXNl","utf8")):
        print("hello")

def create_one_time_rotor_setting():
    OTR = ""
    while True:
        for rotor in range(0,3):
            OTR = OTR + str(random.randint(0,9))
        time.sleep(ONE_TIME_ROTOR_SETTING)
        print(OTR)
        return OTR



HOST, PORT, BUFFER_SIZE, ONE_TIME_ROTOR_SETTING = import_settings()
SERVER = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST,PORT)
SERVER.bind(ADDR)

def main():

    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accept_incomming_connection).start()
    ACCEPT_THREAD.join()
    SERVER.close()

main()