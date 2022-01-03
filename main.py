from flask import Flask
from datetime import datetime
from flask import render_template
from flask.json import tojson_filter

app = Flask(__name__)


# @app.route('/')
# def index():
#     return "hello wrold!123!"


@app.route('/today')
def today():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date


@app.route('/h2')
def h2():
    h2 = """
        <table border="1"><thead>
        <th>期數</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        </thead></table>
    
    """
    return h2


@app.route('/sum/x=<a>&y=<b>', methods=['GET'])
def get_sum(a, b):
    total = eval(a)+eval(b)
    return str(total)


@app.route("/bmi/name=<name> &height=<height>&weight=<weight>", methods=['GET'])
def bmi(name, height, weight):
    bmi = eval(height)/(eval(weight)**2)
    return f'{name} bmi數值為:{bmi}'


@app.route('/')
def index():
    return render_template('./index.html')


if __name__ == "__main__":
    app.run(debug=True)
