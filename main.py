"""
This function will sit and wait based on a parameter that is passed in.
"""

from time import sleep
import json
import os

from textblob import TextBlob

def hello():
    message = "Hello from Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    with open("hello.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact

def hangout(duration):
    sleep(duration)

def translate(messagedata, lang):
    data_dict = {}
    with open(messagedata,'r') as f:
        data_dict = json.load(f)
    message = TextBlob(data_dict["message"])
    message_dict = {}
    message_dict["message"] = message.translate(to=lang).string
    message_dict["schema"] = "message"
    with open("translated.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) #

def hello_translate(lang):
    message = TextBlob("Hello from Orquestra!")
    message_dict = {}
    if lang == 'en':
        message_dict["message"] = message.string
    else:
        message_dict["message"] = message.translate(to=lang).string
    message_dict["schema"] = "message"
    with open("hello.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact

def environment_variables():
    message_dict = {}
    message_dict["env-variables"] = dict(os.environ)
    message_dict["schema"] = "envvariables"
    with open("envvars.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # W

hello_translate("en")