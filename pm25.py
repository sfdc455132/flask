import pandas as pd
url = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv'
df = pd.read_csv(url).dropna()


def get_county():
    cityss = []
    for ci in df['county']:
        if ci not in cityss:
            cityss.append(ci)
    cityss = cityss[1:]+cityss[0:1]
    return cityss


def get_county_pm25(county):
    return df.groupby('county').get_group(county).get(['Site', 'PM25']).values.tolist()


def get_six_pm25():
    six_cities = ["臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市"]
    six_pm25 = {}
    for city in six_cities:
        pm25 = round(df.groupby('county').get_group(
            city).get('PM25').mean(), 2)
        six_pm25[city] = pm25
    return six_pm25


def get_pm25(type=0):
    columns = ['Site', 'county', 'PM25']
    datas = df[columns].values.tolist()
    if type == 1:
        datas = sorted(datas, key=lambda x: x[-1], reverse=True)
    if type == 2:
        datas = sorted(datas, key=lambda x: x[-1], reverse=False)
    if type == 0:
        datas = df[columns].values.tolist()
    return datas, columns, df
