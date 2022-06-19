# app.py
# Markie Personal site

version = "0.0.1"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worlde!"

if __name__ == '__main__':
    app.run(debug=True)
