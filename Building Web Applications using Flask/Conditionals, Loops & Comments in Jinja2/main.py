from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    marks = {
        "Bhavani": 90,
        "Siddharth": 98,
        "Dhanraj": 89
    }
    return render_template("index.html")

app.run(port=5000,debug=True)