import math
import datetime
import itemCFEval
from _collections import defaultdict
from _operator import itemgetter

#读取文件
def readFile(fileData):
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
def measureSimilarity(user_dict):
    N = dict()
    C = defaultdict(defaultdict)
    W = defaultdict(defaultdict)
    for key in user_dict:
        for i in user_dict[key]:
            if i[0] not in N.keys():    
                N[i[0]] = 0
            N[i[0]] += 1                
            for j in user_dict[key]:
                if i == j:
                    continue
                if j[0] not in C[i[0]].keys():
                    C[i[0]][j[0]] = 0
                C[i[0]][j[0]] += 1      
    for i, related_item in C.items():
        for j, cij in related_item.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W

#结合用户喜好对物品排序
def recommond(resultPath, user_count, user_dict, K, topN):
    W = measureSimilarity(user_dict)
    f = open(resultPath, "w")
    user_id = 1
    while user_id <= user_count:
        rank = defaultdict(int) #the most important word and easy to write in the wrong site
        for i, score in user_dict[user_id]: 
            for j, wj in sorted(W[i].items(), key = itemgetter(1), reverse=True)[0:K]: 
                if j in user_dict[user_id]:
                    continue
                rank[j] += score * wj       
        l = sorted(rank.items(), key = itemgetter(1), reverse = True)[0:topN]
        for item in l:
            f.write(str(user_id) + ' | ' + str(item[0]))
            f.write("\n")
        user_id += 1
        
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

def recoAndEval(trainPath, testPath, resultPath, topN, K, userCount, totalUserCount, totalItemCount):
    print("---------K = " + str(K) + ", top" + str(topN) + " recommendation is running !----------")
    d1 = datetime.datetime.now()  
    fileTemp = readFile(trainPath)
    user_dic = createDict(fileTemp)  
    recommond(resultPath, userCount, user_dic, K, topN)   
    d2 = datetime.datetime.now()
    interval = d2 - d1  
    total_sec = interval.total_seconds()  
    print('total time: ' + str(total_sec) + 's')
    correct_ratio = itemCFEval.doEvaluate(topN, userCount, testPath, resultPath, totalUserCount, totalItemCount)
    print("---------recommendation is over !----------")
    return correct_ratio

def newExec(seq):
    filename = 'finalPrecision_top' + str(seq) + '.txt'
    finalFile = open(filename, 'w')
    K = 1
    topN = seq
    trainPath = '../ml-100k/u1.base'
    testPath = '../ml-100k/u1.test'    
    userCount = 450
    totalUserCount = 943
    totalItemCount = 1682
    while K <= 100:
        resultPath = '../recommendResult/result_top' + str(seq) + '_K' + str(K) + '.txt'
        correct_ratio = recoAndEval(trainPath, testPath, resultPath, topN, K, userCount, totalUserCount, totalItemCount)
        finalFile.write('K = ' + str(K) + ', top' + str(topN) + ': correct ratio = ' + str(correct_ratio) + '\n')
        finalFile.write('------------------------------------------------\n')
        K += 1
    
#主程序
if __name__ == '__main__':
    begin = 1
    end = 25
    while begin <= end:
        newExec(begin)
        begin += 1 