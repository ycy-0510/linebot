import requests

def getBus():
    req = requests.get('https://tdx.transportdata.tw/api/basic/v2/Bus/EstimatedTimeOfArrival/City/Taipei/265%E5%8D%80?%24orderby=Direction&%24format=JSON'
                                   ,headers={
                                       'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                                   }).json()
    info = ''
    for i in range(0,2):
        info = f'{info}=====方向:{["去","回"][i]}=====\n'
        for item in req:
            if item["Direction"] == i:
                info=f'{info}{item["StopName"]["Zh_tw"]} 時間：{round(item["EstimateTime"]/60) if item["StopStatus"]==0 else "未發車"}\n'
    return info