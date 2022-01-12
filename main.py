from flask import Flask, request
from datetime import date, datetime
from flask import render_template
from flask.json import tojson_filter
import pandas as pd
from pm25 import get_pm25, get_six_pm25, get_county_pm25
import json

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


@app.route('/')
def index():
    name = '741'
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]
    # HTML 那邊需改成<>{{name}}<>
    return render_template('./index.html', **locals())
    # context={'name':name,'date':date}
    # HTML那邊需改成 <>context[name]<>


@app.route('/pm25', methods=["GET", "POST"])
def pm25():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if request.method == 'GET':
        datas, columns = get_pm25(type=0)
    if request.method == "POST":
        if request.form.get('ascending'):
            datas, columns = get_pm25(type=2)
            print('ascending')
        else:
            datas, columns = get_pm25(type=1)
            print('reverse')
    return render_template('./pm25.html', **locals())


@app.route('/county-pm25/<string:county>')
def county_pm25_get(county):
    datas = get_county_pm25(county)
    sites = [da[0] for da in datas]
    pm25 = [da[1] for da in datas]

    return json.dumps({'sites': sites, 'pm25': pm25}, ensure_ascii=False)


@app.route('/pm25-echart', methods=['GET', 'POST'])
def pm25_echart():
    return render_template('./pm25-echart.html')


@app.route('/six-pm25', methods=['GET', 'POST'])
def six_pm25():
    six_pm25 = get_six_pm25()
    citys = list(six_pm25.keys())
    pm25 = list(six_pm25.values())

    return json.dumps({'citys': citys, 'pm25': pm25}, ensure_ascii=False)


@app.route('/pm25-data', methods=['GET', 'POST'])
def pm25_data_json():
    values, columns, df = get_pm25(type=0)
    sites = [value[0] for value in values]
    pm25_da = [value[-1] for value in values]
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pm25_datas = [[da[0], da[-1]] for da in values]
    pm25_datas = sorted(pm25_datas, key=lambda x: x[-1])
    highest = pm25_datas[-1]
    lowest = pm25_datas[0]

    datas = {'time': time, 'sites': sites, 'pm25_da': pm25_da,
             'highest': highest, 'lowest': lowest}
    return json.dumps(datas, ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)
