from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller

app = Flask(__name__)

def get_conf():
    with open("config") as file:
        lines = file.read().strip().split("\n")
        quantity = int(lines[0])
        keys = lines[1].strip().split(",")
        file.close()
        return (quantity, keys)

@app.route("/hello")
def helloWorld():
    return "hello world"

@app.route("/config", methods=["Get", "POST"])
def config():
    if request.method == 'POST':
        print(request.form['quantity'])
        with open("config", "r") as file:
            data = file.readlines()
        
        data[0] = request.form['quantity'] + "\n"

        with open("config", "w") as file:
            file.writelines(data)

    return render_template("config.html")

@app.route("/shorty")
def shorty():
    return render_template("shorty.html", quantity=get_conf()[0], keys=get_conf()[1])

keyboard = Controller()

@app.route("/shortcut/<button>")
def shortcut(button):
    eval("keyboard.press(Key." + button + ")")
    eval("keyboard.release(Key." + button + ")")
    print(get_conf()[1])
    return render_template("shorty.html", quantity=get_conf()[0], keys=get_conf()[1])