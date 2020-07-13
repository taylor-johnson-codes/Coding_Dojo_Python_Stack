# Platform lecture
# This will be our "server" file where we will set up all of our routes to handle requests.

from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"; __name__ is a built-in variable to every .py file
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module; if you print(__name__) the output is __main__
    # app.run(debug=True)    # Run the app in debug mode; THIS NEED TO BE THE VERY LAST LINE OF CODE IN THE FILE!
# running this has server running and listening on port 5000


# ROUTING
# Every route has two parts: 1. HTTP method (GET, POST, PUT, PATCH, DELETE)  2. URL

@app.route('/success')
def success():
    return "success"

@app.route('/hello_to_you/<name>')  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello_to_you(name):
    print(name)
    return f"Hello, {name}!"

@app.route('/users/<username>/<id>')  # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return f"username: {username}, id: {id}"

@app.route("/hello")
def hello():
    return render_template("index.html")  # added render_template to import line

@app.route("/example")
def example():
    return render_template("index.html", phrase="hello", times=10)  # added two more args for the HTML file

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("index2.html", random_numbers = [3,1,5], students = student_info)






if __name__=="__main__":
    app.run(debug=True)