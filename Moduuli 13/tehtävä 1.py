from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def hello():

    return "Terve maailma"

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)