from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/secondpage")
def func():
    var = "return this variable"
    return var

if __name__ == "__main__":
    app.run()