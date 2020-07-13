# Platform lecture

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"  # secret key is required for session

# the index route just shows the form; it doesn't process the form
@app.route('/')
def index():
    return render_template("index.html")

# this route actually handles the form
@app.route('/users', methods=['POST'])  # this route only accepts post requests
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
    return redirect("/show")

@app.route('/show')
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    # return render_template("show.html", name_on_template="session['username'], email_on_template=session['useremail']")
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)