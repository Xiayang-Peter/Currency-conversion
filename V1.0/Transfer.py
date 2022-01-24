lang=input("输入CN使用中文界面\ntype EN to use english interface:")

import time
localtime = time.localtime(time.time())
time = time.strftime("%Y-%m-%d %H:%M:%S",localtime)

import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/NZD/CNY' 
response = requests.get(url)    
NZD_TO_CNY = response.json()  
NZD_TO_CNY = NZD_TO_CNY['conversion_rate']
#4.2713
CNY_TO_NZD = 100/ (100 * NZD_TO_CNY)
CNY_TO_NZD = round(CNY_TO_NZD,4)

while lang == "CN":
    CURRENCY=(input("请选择货币（1为CNY，2为NZD）"))
    currency=(int(CURRENCY))
    if currency == 1:                                              #人民币转纽币
        print("CNY--->NZD")
        print("当前汇率为:",CNY_TO_NZD)
        TOTALrmb=(input("输入CNY数量："))
        totalrmb=(int(TOTALrmb))
        print("总共", totalrmb * CNY_TO_NZD,"NZD")
    elif currency == 2:                                              #纽币转人民币
        print("NZD--->CNY")
        print("当前汇率为:",NZD_TO_CNY)
        TOTALnzd=(input("输入NZD数量："))
        totalnzd=(int(TOTALnzd))
        print("总共", totalnzd * NZD_TO_CNY,"CNY")
 ##############
    for EN in lang:
        CURRENCY=(input("please select your currency（1=CNY，2=NZD）"))
        currency=(int(CURRENCY))
    if currency == 1:                                              #人民币转纽币
        print("CNY--->NZD")
        print("The current exchange rate is:",CNY_TO_NZD)
        TOTALrmb=(input("Enter the amount of CNY："))
        totalrmb=(int(TOTALrmb))
        print("total", totalrmb*CNY_TO_NZD,"NZD")

    elif currency == 2:                                              #纽币转人民币
        print("NZD--->CNY")
        print("The current exchange rate is:",NZD_TO_CNY)
        TOTALnzd=(input("Enter the amount of NZD："))
        totalnzd=(int(TOTALnzd))
        print("total", totalnzd*NZD_TO_CNY,"CNY")
        print("1=CNY,2=NZD")

    state=(input("exit？（1=exit;2=continue）："))
    state=int(state)
    
    if state ==2:                                                  #是否退出？
        print("continue")
    elif state ==1:                                                 #是否退出？
        exit()   
    else:
        print("请输入CN或NZn/please type CN or NZ:")     

    



    #print(type(currency))



















'''    
while lang == "EN":
    CURRENCY=(input("please select your currency（1=CNY，2=NZD）"))
    currency=(int(CURRENCY))
    if currency == 1:                                              #人民币转纽币
        print("CNY--->NZD")
        print("The current exchange rate is:",data2)
        TOTALrmb=(input("Enter the amount of CNY："))
        totalrmb=(int(TOTALrmb))
        print("total", totalrmb*data2,"NZD")
    elif currency == 2:                                              #纽币转人民币
        print("NZD--->CNY")
        print("The current exchange rate is:",data)
        TOTALnzd=(input("Enter the amount of NZD："))
        totalnzd=(int(TOTALnzd))
        print("total", totalnzd*data,"CNY")
        print("1=CNY,2=NZD")
    state=(input("exit？（1=exit;2=continue）："))
    state=int(state)
    if state ==2:                                                  #是否退出？
        print("continue")
    elif state ==1:                                                 #是否退出？
        exit()   
    else:
      print("请输入CN或NZn/please type CN or NZ:")                                            
      
if lang == "fixmode":
    print('NZD-->CNY API',dataO1)
    print('CNY-->NZD API',dataO2)
    exit()
























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


    



 url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/CNY/NZD'
 response1 = requests.get(url)    
 carrencydata1 = response1.json()
 print(carrencydata1['conversion_rate'])
 '''