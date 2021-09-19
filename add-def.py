"""
lang=input("输入CN使用中文界面\ntype EN to use english interface:")
import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/NZD/CNY' # api所在url
response = requests.get(url)    # 从url获取并赋值data
dataO1 = response.json()  # 从url获取并赋值data
# 输出api返回信息（保留）
#print(data)
try:
    data=str(dataO1) #转换为string
    data=(data[391:397]) 
    data=float(data)
except:
    print("api数据错误")
#print("当前比率为:",data)
import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/CNY/NZD' # api所在url
response2 = requests.get(url)    # 从url获取并赋值data
dataO2 = response2.json()  # 从url获取并赋值data
# 输出api返回信息（保留）
#print(data2)
try:
    data2 = str(dataO2) #转换为string
    data2 = (data2[391:396]) 
    data2 = float(data2)
except:
    print("api数据错误")
"""

c1