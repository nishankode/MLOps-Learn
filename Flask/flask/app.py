from flask import Flask 

# Creating an instance of flask class which will be the WSGI.
app = Flask(__name__)

# Creating a basic route
@app.route("/")
def welcome():
    return "Welcome to this flask course"

# Creating sample index route
@app.route("/index")
def index():
    return "welcome to the index page"


if __name__ == '__main__':
    app.run(debug=True)