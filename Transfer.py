#记得检查更新！！！
#pip install requests
#test 1

lang=input("输入CN使用中文界面\ntype EN to use english interface:")
import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/NZD/CNY' # api所在url
response = requests.get(url)    # 从url获取并赋值data
dataO1 = response.json()  # 从url获取并赋值data
# 输出api返回信息（保留）
#print(data)
data=str(dataO1) #转换为string
data=(data[391:397]) 
data=float(data)
#print("当前比率为:",data)
import requests
url= 'https://v6.exchangerate-api.com/v6/c24594258bb5eec9b26a0950/pair/CNY/NZD' # api所在url
response2 = requests.get(url)    # 从url获取并赋值data
dataO2 = response2.json()  # 从url获取并赋值data
# 输出api返回信息（保留）
#print(data2)
data2=str(dataO2) #转换为string
data2=(data2[391:396]) 
data2=float(data2)
#print("当前比率为:",data2)

while lang == "CN":
    CURRENCY=(input("请选择货币（1为CNY，2为NZD）"))
    currency=(int(CURRENCY))
    if currency == 1:                                              #人民币转纽币
        print("CNY--->NZD")
        print("当前汇率为:",data2)
        TOTALrmb=(input("输入CNY数量："))
        totalrmb=(int(TOTALrmb))
        print("总共", totalrmb*data2,"NZD")
    elif currency == 2:                                              #纽币转人民币
        print("NZD--->CNY")
        print("当前汇率为:",data)
        TOTALnzd=(input("输入NZD数量："))
        totalnzd=(int(TOTALnzd))
        print("总共", totalnzd*data,"CNY")
    else:
        print("1=CNY,2=NZD")
    state=(input("是否退出？（按1退出按2继续）："))
    state=int(state)
    if state ==2:                                                  #是否退出？
        print("继续转换")
    elif state ==1:                                                  #是否退出？
        exit()
    else:
      print("请输入CN或NZn/please type CN or NZ:")

    
    #print(type(currency))
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



