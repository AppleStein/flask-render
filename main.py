from crypt import methods
from django.shortcuts import render
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mainpage():
    return render.template("mainpage.html")

@app.route("/", methods=["GET", "POST"])
def namepage():
    return render.template("name.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)