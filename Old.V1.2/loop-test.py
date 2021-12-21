names=("peter,peter1peter2")
for name in names:
    if name == 'peter1':
        print("你好，peter1")
        break
    print("循环数据"+name)
else:
    print("没有循环数据")
print("完成循环")