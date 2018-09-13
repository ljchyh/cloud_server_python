from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World111!"

@app.route("/user/<name>")
def user(name):
    return "Hello," + name

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='32.221.175.37', port=1111)
