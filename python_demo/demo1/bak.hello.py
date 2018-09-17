from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Worl111d!"

if __name__ == "__main__":
    app.run()
    #app.run(host='32.221.175.37', port=1111)
