from flask import Flask, request
from datetime import date, datetime
from flask import render_template
from flask.json import tojson_filter
import pandas as pd
from pm25 import get_pm25
app = Flask(__name__)


# @app.route('/')
# def index():
#     return "hello wrold!123!"


# @app.route('/today')
# def today():
#     date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     return date


# @app.route('/h2')
# def h2():
#     h2 = """
#         <table border="1"><thead>
#         <th>期數</th>
#         <th>1</th>
#         <th>2</th>
#         <th>3</th>
#         <th>4</th>
#         <th>5</th>
#         <th>6</th>
#         </thead></table>

#     """
#     return h2


# @app.route('/sum/x=<a>&y=<b>', methods=['GET'])
# def get_sum(a, b):
#     total = eval(a)+eval(b)
#     return str(total)


# @app.route("/bmi/name=<name> &height=<height>&weight=<weight>", methods=['GET'])
# def bmi(name, height, weight):
#     bmi = eval(height)/(eval(weight)**2)
#     return f'{name} bmi數值為:{bmi}'


# @app.route('/')
# def index():
#     name = '741'
#     date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     stocks = [
#         {'分類': '日經指數', '指數': '22,920.30'},
#         {'分類': '韓國綜合', '指數': '2,304.59'},
#         {'分類': '香港恆生', '指數': '25,083.71'},
#         {'分類': '上海綜合', '指數': '3,380.68'}
#     ]
#     # HTML 那邊需改成<>{{name}}<>
#     return render_template('./index.html', **locals())
#     # context={'name':name,'date':date}
#     # HTML那邊需改成 <>context[name]<>


@app.route('/', methods=["GET", "POST"])
def pm25():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if request.method == 'GET':
        datas, columns = get_pm25(sort='5')
    if request.method == "POST":
        if request.form.get('ascending'):
            datas, columns = get_pm25()
            print('ascending')
        else:
            datas, columns = get_pm25(sort=True)
            print('reverse')
    return render_template('./pm25.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)
