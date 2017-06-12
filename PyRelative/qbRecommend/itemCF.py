import math
import datetime
import itemCFEval
from _collections import defaultdict
from _operator import itemgetter

#读取文件
def readFile(fileData):
    begin_readFile = datetime.datetime.now();
    rates = []
    f = open(fileData, "r")
    data = f.readlines()
    f.close()
    for line in data:
        dataLine = line.split("\t")
        rates.append([int(dataLine[0]), int(dataLine[1]), int(dataLine[2])])
    end_readFile = datetime.datetime.now();
    interval_readFile = end_readFile - begin_readFile  
    total_sec_readFile = interval_readFile.total_seconds()  
    print("(0) read file completed. total time use : " + str(total_sec_readFile) + "s")
    return rates

#创建字典，生成用户评分的数据结构
#    输入：数据集合，格式：user id | item id | rating | timestamp. 
#    输出：user_dict[user id]=[(item id，rating)...]
def createDict(rates):
    begin_createDict = datetime.datetime.now();
    user_dict = {}
    for i in rates:
        if i[0] in user_dict:
            user_dict[i[0]].append((i[1], i[2]))
        else:
            user_dict[i[0]] = [(i[1], i[2])]
    end_createDict = datetime.datetime.now();
    interval_createDict = end_createDict - begin_createDict  
    total_sec_createDict = interval_createDict.total_seconds()  
    print("(1) create user_dict completed. total time use : " + str(total_sec_createDict) + "s")
    return user_dict

#建立物品倒排表，计算物品相似度
def itemCF(user_dict):
    begin_itemCF = datetime.datetime.now();
    N = dict()
    C = defaultdict(defaultdict)
    W = defaultdict(defaultdict)
    begin_firstLoop = datetime.datetime.now();
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
    end_firstLoop = datetime.datetime.now();
    interval_firstLoop = end_firstLoop - begin_firstLoop  
    total_sec_firstLoop = interval_firstLoop.total_seconds()  
    print("(2.1) first loop of inverted list completed. total time use : " + str(total_sec_firstLoop) + "s")
    begin_secondLoop = datetime.datetime.now();
    for i, related_item in C.items():
        for j, cij in related_item.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    end_secondLoop = datetime.datetime.now();
    interval_secondLoop = end_secondLoop - begin_secondLoop  
    total_sec_secondLoop = interval_secondLoop.total_seconds()  
    print("(2.2) second loop of inverted list completed. total time use : " + str(total_sec_secondLoop) + "s")
    end_itemCF = datetime.datetime.now();
    interval_itemCF = end_itemCF - begin_itemCF  
    total_sec_itemCF = interval_itemCF.total_seconds()  
    print("(2) create user-item inverted list completed. total time use : " + str(total_sec_itemCF) + "s")
    return W

#结合用户喜好对物品排序
def recommondation(user_count, user_dict, K):
    rank = defaultdict(int)
    W = itemCF(user_dict)
    begin_recommondation = datetime.datetime.now();
    f = open("result.txt", "w")
    user_id = 1
    while user_id <= user_count:
        for i, score in user_dict[user_id]: #i为特定用户的电影id，score为其相应评分
            for j, wj in sorted(W[i].items(), key = itemgetter(1), reverse=True)[0:K]: #sorted()的返回值为list，List的元素为元组
                if j in user_dict[user_id]:
                    continue
                rank[j] += score * wj       #先找出用户评论过的电影集合，对每一部电影id，找出与该电影最相似的K部电影，计算出在id下用户对每部电影的兴趣度，接着迭代整个用户评论过的电影集合，求加权和，再排序，可推荐出前n部电影
        l = sorted(rank.items(), key = itemgetter(1), reverse = True)[0:10]
        for item in l:
            f.write(str(user_id) + ' | ' + str(item[0]))
            f.write("\n")
        user_id += 1
    end_recommondation = datetime.datetime.now();
    interval_recommondation = end_recommondation - begin_recommondation  
    total_sec_recommondation = interval_recommondation.total_seconds()  
    print("(3) sorted and recommend completed. total time use : " + str(total_sec_recommondation) + "s")

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

#主程序
if __name__ == '__main__':
    print("recommendation is running !")
    d1 = datetime.datetime.now()  
    fileTemp = readFile("../ml-100k/u1.base")             #读取文件
    user_dic = createDict(fileTemp)  #创建字典
    user_count = 450
    f = open("result.txt", "w")
    recommondation(user_count, user_dic, 85)   
    d2 = datetime.datetime.now()
    interval = d2 - d1  
    total_sec = interval.total_seconds()  
    print('total time: ' + str(total_sec) + 's')
    itemCFEval.doEvaluate(10, user_count)