'''
Created on 2017年6月6日

@author: HotGaoGao
'''
import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 100:
#         time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))
    print("end")
    
try:
    _thread.start_new_thread(print_time, ("Thread-1", 0))
    _thread.start_new_thread(print_time, ("Thread-2", 0))
    print("aaaaaaaaaaaaaa")
except:
    print("Error: 无法启动线程")
    
while 1:
    pass