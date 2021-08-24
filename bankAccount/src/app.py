from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome_test():
    return 'Running on PORT: 5000'