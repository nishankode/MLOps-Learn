from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def get_home_page():
    return "<h1>Welcome to the home page</h1>"

@app.route("/index")
def get_index_page():
    return render_template("index.html")

@app.route("/about")
def get_about_page():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def greet():
    if request.method == 'POST':
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template("form.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if username == 'nishan' and password == 'nishan':
            return render_template('about.html')
        else:
            return "<h1>Invalid Login Credentials</h1>"
    return render_template("miscform.html")


if __name__ == "__main__":
    app.run()