
# cd P:\临时\python path to file
# 文件名： exchange-api.py


import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/NZD/CNY' # api所在url
response = requests.get(url)    # 从url获取并赋值data
odata = response.json()  # 从url获取并赋值data
# 输出api返回信息（保留）
#print(data)
data=str(odata) #转换为string
data=(data[391:397]) 
data=float(data)
print("当前比率为:",data)
print(type(odata))

