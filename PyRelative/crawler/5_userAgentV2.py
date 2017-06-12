'''
Created on 2017年5月16日

@author: HotGaoGao
'''
import urllib
import http.cookiejar
import time

def saveFile(data):
    ISOTIMEFORMAT = '%Y_%m_%d_%X'
    t = time.strftime(ISOTIMEFORMAT, time.localtime())
    t = t.replace(':', '_')
    save_path = '../crawlerResult/' + t + '.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()
    
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()
uop = oper.open('http://www.baidu.com', timeout = 1000)
data = uop.read()
saveFile(data)
print(data.decode())