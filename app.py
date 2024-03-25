from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def helloWorld():
    return "hello world"

@app.route("/config")
def config():
    return render_template("config.html")

with open("config") as file:
    lines = file.read().strip().split("\n")
    quantity = int(lines[0])
    


@app.route("/shorty")
def shorty():
    
    return render_template("shorty.html", quantity=quantity)