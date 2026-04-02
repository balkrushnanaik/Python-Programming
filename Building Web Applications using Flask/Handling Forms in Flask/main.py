from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"] )
def hello_world():
    if request.method == "POST":
        # Handle the form
        with open("file.txt", "w") as f:
            f.write(f"The name is {request.form['name']}, email is {request.form['email']}  and message is {request.form['message']}")
    return render_template("contact.htm")

app.run(port=8000, debug=True)