'''
Created on 2017年6月8日

@author: HotGaoGao
'''
import math
from _collections import defaultdict
from _operator import itemgetter

def readFile(fileData):
    rates = []
    f = open(fileData, "r")
    data = f.readlines()
    f.close()
    for line in data:
        dataLine = line.split("\t")
        rates.append([int(dataLine[0]), int(dataLine[1]), int(dataLine[2])])
    return rates

def createDict(rates):
    user_dict = {}
    for i in rates:
        if i[0] in user_dict:
            user_dict[i[0]].append((i[1], i[2]))
        else:
            user_dict[i[0]] = [(i[1], i[2])]
    return user_dict

def itemCF(user_dict):
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

def recommondation(user_id, user_dict, K):
    rank = defaultdict(int)
    W = itemCF(user_dict)
    for i, score in user_dict[user_id]:
        for j, wj in sorted(W[i].items(), key = itemgetter(1), reverse=True)[0:K]: 
            if j in user_dict[user_id]:
                continue
            rank[j] += score * wj       
    l = sorted(rank.items(), key = itemgetter(1), reverse = True)[0:20]
    return l

fileTemp = readFile("u1test.base") 
user_dic = createDict(fileTemp)
user_id = 1
movieTemp = recommondation(user_id, user_dic, 80)  #对电影排序   
for i in movieTemp:
    print(str(user_id) + " | " + str(i[0]))