from flask import Flask,jsonify
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World112!"

@app.route("/user/<name>")
def user(name):
    return "Hello," + name

@app.route("/json")
def try_json():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='32.221.175.37', port=1111)
