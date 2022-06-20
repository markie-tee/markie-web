# app.py

# Markie Personal site

version = "0.0.1"

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
            'index.html',title='summer nights in the grass')

if __name__ == '__main__':
    app.run(developement=True)
