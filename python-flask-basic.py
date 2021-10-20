from flask import Flask
# from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

@app.route("/say-somthing")
def say_something():
    return '<h1 style="color: red;">Hello everyone!</h1>'

@app.route("/console-log")
def console_log():
    print("hello")
    return 'Hello'

if __name__ == "__main__":
    app.run(debug=True)