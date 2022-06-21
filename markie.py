# app.py

# Markie Personal site

version = "0.1.1"

from flask import Flask, render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    return render_template(
            'index.html',title='summer nights in the grass')

if __name__ == '__main__':
    app.run(developement=True)
