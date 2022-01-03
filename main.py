from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return "hello wrold!123!"


@app.route('/today')
def today():
    date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return date


if __name__ == "__main__":
    app.run(debug=True)
