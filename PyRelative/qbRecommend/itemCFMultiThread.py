import math
import datetime
import _thread
import time
from _collections import defaultdict
from _operator import itemgetter
from prettytable import PrettyTable
#读取文件
def readFile(fileData):
    data = []
    rates = []
    f = open(fileData, "r")
    data = f.readlines()
    f.close()
    for line in data:
        dataLine = line.split("\t")
        rates.append([int(dataLine[0]), int(dataLine[1]), int(dataLine[2])])
    return rates

#创建字典，生成用户评分的数据结构
#    输入：数据集合，格式：user id | item id | rating | timestamp. 
#    输出：user_dict[user id]=[(item id，rating)...]
def createDict(rates):
    user_dict = {}
    for i in rates:
        if i[0] in user_dict:
            user_dict[i[0]].append((i[1], i[2]))
        else:
            user_dict[i[0]] = [(i[1], i[2])]
    return user_dict

#建立物品倒排表，计算物品相似度
def itemCF(user_dict):
    N = dict()
    C = defaultdict(defaultdict)
    W = defaultdict(defaultdict)
    for key in user_dict:
        for i in user_dict[key]:
            if i[0] not in N.keys():    #i[0]表示movie_id
                N[i[0]] = 0
            N[i[0]] += 1                #N[i[0]]表示评论过某电影的用户数                
            for j in user_dict[key]:
                if i == j:
                    continue
                if j[0] not in C[i[0]].keys():
                    C[i[0]][j[0]] = 0
                C[i[0]][j[0]] += 1      #C[i[0]][j[0]]表示电影两两之间的相似度，eg：同时评论过两个电影的用户数
    for i, related_item in C.items():
        for j, cij in related_item.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
#             print(W[i][j])
#             print(cij)
#             print(math.sqrt(N[i] * N[j]))
    return W

#结合用户喜好对物品排序
def recommondation(user_id, user_dict, K):
    rank = defaultdict(int)
    l = list()
    W = itemCF(user_dict)
    for i, score in user_dict[user_id]: #i为特定用户的电影id，score为其相应评分
        for j, wj in sorted(W[i].items(), key = itemgetter(1), reverse=True)[0:K]: #sorted()的返回值为list，List的元素为元组
            if j in user_dict[user_id]:
                continue
            rank[j] += score * wj       #先找出用户评论过的电影集合，对每一部电影id，假设其中一部电影id1，找出与该电影最相似的K部电影，计算出在id1下用户对每部电影的兴趣度，接着迭代整个用户评论过的电影集合，求加权和，再排序，可推荐出前n部电影
    l = sorted(rank.items(), key = itemgetter(1), reverse = True)[0:20]
    return l

#获取电影列表
def getMovieList(item):
    items = {}
    f = open(item, "r")
    movie_content = f.readlines()
    f.close()
    for movie in movie_content:
        movieLine = movie.split("|")
        items[int(movieLine[0])] = movieLine[1:]
    return items

def executeSingle(begin, end, itemList, dic, delay):
    time.sleep(delay)
    user_id = begin
    user_count = end
    while user_id <= user_count :
        movieTemp = recommondation(user_id, dic, 80)  #对电影排序
        for i in movieTemp:
            temp = itemList.get(i[0])
            if temp != None:
                f.write(str(user_id) + " | " + str(i[0]))
                f.write("\n")      
        user_id += 1
    d2 = datetime.datetime.now()
    interval = d2 - d1  
    total_sec = interval.total_seconds()  
    print(str(begin) + ' total time: ' + str(total_sec) + 's')

#主程序
if __name__ == '__main__':
    d1 = datetime.datetime.now()  
    itemTemp = getMovieList("u.item")         #获取电影列表
    fileTemp = readFile("u.data")             #读取文件
    user_dic = createDict(fileTemp)  #创建字典
    user_id = 1
    user_count = 100
    f = open("result.txt", "w")
    _thread.start_new_thread(executeSingle, (1, 13, itemTemp, user_dic, 0.2))
    _thread.start_new_thread(executeSingle, (14, 26, itemTemp, user_dic, 0.3))
    _thread.start_new_thread(executeSingle, (27, 39, itemTemp, user_dic, 0.4))
    _thread.start_new_thread(executeSingle, (40, 52, itemTemp, user_dic, 0.5))
    _thread.start_new_thread(executeSingle, (53, 65, itemTemp, user_dic, 0.6))
    _thread.start_new_thread(executeSingle, (66, 78, itemTemp, user_dic, 0.7))
    _thread.start_new_thread(executeSingle, (79, 90, itemTemp, user_dic, 0.8))
    _thread.start_new_thread(executeSingle, (91, 100, itemTemp, user_dic, 0.9))
#     d2 = datetime.datetime.now()  
#     interval = d2 - d1  
#     total_sec = interval.total_seconds()  
#     print('total time: ' + str(total_sec) + 's')
    while 1:
        pass
    print("--------------Successfully End--------------")