#api
import requests

url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/NZD/CNY'
response = requests.get(url)    
api = response.json()
rate = (api['conversion_rate'])
float(rate)

import time
localtime = time.localtime(time.time())
time = time.strftime("%Y-%m-%d %H:%M:%S",localtime)

for check in api:
    if check == 'conversion_rate':
        lang = input("输入CN使用中文界面\ntype EN to use english interface:")
        lang.upper()
    else:
        print('未知错误',exit())
    if lang == 'CN':
        print('本地时间:',time)
        print('当前汇率为:',)


        


    



# while lang == "CN":


    



'''
 url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/CNY/NZD'
 response1 = requests.get(url)    
 carrencydata1 = response1.json()
 print(carrencydata1['conversion_rate'])
 '''