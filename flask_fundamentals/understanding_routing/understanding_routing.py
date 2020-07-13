# first open terminal and activate environment
# test a lot along the way to easily find bugs (aka breakpoints)

# # the first breakpoint to run to make sure Flask server is running:
# from flask import flask
# app = Flask(__name__)
# app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<word>")  # variable signified by <>
def word_method(word):  # parameter must be variable
    print(word)
    return f"Hi {word}!"

# create 2 URL path variables (amount and word); URL numbers are strings
@app.route("/repeat/<word>/<num>")
def repeat(word, num):
    return (word)*int(num)  # cast URL str into int

app.run(debug=True)