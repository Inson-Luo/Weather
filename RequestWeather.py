"""Get weather"""

import requests
import json

def GetWeather(cityName):
    urlAll = 'http://www.nmc.cn/rest/province/all'
    url_weather = 'http://www.nmc.cn/rest/weather'

    headers = {
        'Host': 'www.nmc.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    param = {
        '_': '1659336731518'
    }

    resProvinceAll = requests.get(url=urlAll, params=param, headers=headers)
    dataProvinceAll = resProvinceAll.text
    contentProvinceAll = json.loads(dataProvinceAll)
    flag = 0
    for cPA in contentProvinceAll:
        urlProvince = 'http://www.nmc.cn/rest/province/' + cPA['code']

        resProvince = requests.get(url=urlProvince, params=param, headers=headers)
        dataProvince = resProvince.text
        contentProvince = json.loads(dataProvince)
        for cP in contentProvince:
            if cityName in cP['city']:
                param['stationid'] = cP['code']
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        resWeather = requests.get(url=url_weather, params=param, headers=headers)
        dataresWeather = resWeather.text
        contentresWeather = json.loads(dataresWeather)
        return [contentresWeather['data']['real']['weather']['temperature'], contentresWeather['data']['real']['weather']['info']]
    else:
        return []
