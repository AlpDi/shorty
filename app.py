from flask import Flask, render_template, request, jsonify
from pynput.keyboard import Key, Controller
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conf():
    with open("config") as file:
        lines = file.read().strip().split("\n")
        quantity = int(lines[0])
        keys = lines[1].strip().split(" ")
        file.close()
        return (quantity, keys)

@app.route("/hello")
def helloWorld():
    return "hello world"



@app.route("/rest/config", methods=["GET"])
def config():
    with open("config.json") as config_file:
        data = config_file.read()

    parsed_data = json.loads(data)

    return jsonify(parsed_data)

keyboard = Controller()

@app.route("/shortcut/<button>")
def shortcut(button):
    if(button == "dc_mute"):
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press(Key.alt)
        keyboard.press("m")

        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.alt)
        keyboard.release("m")

    if(button == "dc_fullmute"):
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press(Key.alt)
        keyboard.press("d")

        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.alt)
        keyboard.release("d")

    if(button == "media_play_pause"):
        keyboard.press(Key.media_play_pause)
        
        keyboard.release(Key.media_play_pause)
        

    return "key pressed"
        