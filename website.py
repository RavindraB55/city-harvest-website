from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html")   # some basic inline html

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    name = "Ravi"
    app.run(debug = True)
