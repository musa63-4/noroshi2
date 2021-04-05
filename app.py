from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def top():
    return render_template("no.html")

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/")
def members():
    return render_template("members.html")

@app.route("/")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
