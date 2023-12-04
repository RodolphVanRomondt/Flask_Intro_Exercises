# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_route():

    a = request.args["a"]
    b = request.args["b"]
    return f"{add(int(a), int(b))}"

@app.route("/sub")
def sub_route():

    a = request.args["a"]
    b = request.args["b"]
    return f"{sub(int(a), int(b))}"

@app.route("/mult")
def mult_route():

    a = request.args["a"]
    b = request.args["b"]
    return f"{mult(int(a), int(b))}"

@app.route("/div")
def div_route():

    a = request.args["a"]
    b = request.args["b"]
    result = div(int(a), int(b))
    return f"{int(result)}"

@app.route("/math/<operation>")
def math_route(operation):

    a = int(request.args["a"])
    b = int(request.args["b"])
    MATH = {"add": add(a, b), "sub": sub(a, b), "mult": mult(a, b), "div": div(a, b)}
    return f"{MATH[operation]}"