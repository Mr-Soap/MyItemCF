'''
Created on 2017年6月6日

@author: HotGaoGao
'''
import _csv 
import datetime

with open('u.data', 'r', encoding = 'utf-8') as csvfile:
    #读取csv文件，返回的是迭代类型
    read = _csv.reader(csvfile)
    d1 = datetime.datetime.now()  
    for i in read:
        print(i)
    d2 = datetime.datetime.now()  
    interval = d2 - d1  
    total_sec = interval.total_seconds()  
    print('total time: ' + str(total_sec) + 's')