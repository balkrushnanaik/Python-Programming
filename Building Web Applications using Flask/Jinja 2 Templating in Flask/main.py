from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Vaibhav": 90,
        "Siddharth": 98,
        "Dhanraj": 89
    }
    return render_template("index.html", marks=marks)

app.run()