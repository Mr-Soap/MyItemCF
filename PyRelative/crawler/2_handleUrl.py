'''
Created on 2017年5月15日

@author: HotGaoGao
'''
import urllib
import urllib.request

data = {}
data['word'] = 'youdao'

url_values = urllib.parse.urlencode(data)
url = 'http://wwww.baidu.com/s?'
full_url = url + url_values

print(full_url)

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
