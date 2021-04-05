from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route("/")
def top():
    return render_template("no.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/members.html")
def members():
    return render_template("members.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
