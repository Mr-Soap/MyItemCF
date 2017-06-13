'''
Created on 2017年5月15日

@author: HotGaoGao
'''
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)