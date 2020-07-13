# open terminal and activate environment

from flask import Flask, render_template  # needed for using HTML file in app
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/play")
def play():
    return render_template("index.html", times=3)  

@app.route("/play/<qty>")
def boxes(qty):
    return render_template("index.html", times=int(qty))

@app.route("/play/<x>/<color>")
def boxes_color(x, color):
    return render_template("index_color.html", times=int(x), color=color)

if __name__=="__main__":
    app.run(debug=True)