"""
This function will sit and wait based on a parameter that is passed in.
"""

from time import sleep
import json
import os

def hello():
    message = "Hello from Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("hello.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact

def hangout(duration):
    sleep(duration)

def environment_variables():

    message_dict = {}
    message_dict["env-variables"] = message
    message_dict["schema"] = "envvariables"

    with open("envvars.json",'w') as f:
        f.write(json.dumps(dict(os.environ), indent=2)) # W
