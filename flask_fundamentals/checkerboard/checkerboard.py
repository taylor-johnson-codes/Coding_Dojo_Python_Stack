from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route("/")
def index8x8():
    return render_template("index8x8.html")

@app.route("/4")
def index8x4():
    return render_template("index8x4.html")

@app.route("/<x>/<y>")
def index_xy(x,y):
    return render_template("index_xy.html", x=int(x), y=int(y))

if __name__ == "__main__":
    app.run(debug=True)