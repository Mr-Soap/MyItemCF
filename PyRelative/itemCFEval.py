'''
Created on 2017年6月6日

@author: HotGaoGao
'''
def doEvaluate(topN, user_count, testPath, resultPath, totalUserCount, totalItemCount):
    f = open(testPath, 'r')
    data = f.readlines()
    f.close()
    user_dict = dict()
    count_0 = 1
    while count_0 <= totalUserCount:
        count_1 = 1
        user_dict[str(count_0)] = dict()
        while count_1 <= totalItemCount:
            user_dict[str(count_0)][str(count_1)] = 0
            count_1 += 1
        count_0 += 1
    
    for line in data:
        splits = line.split('\t')
        user_dict[splits[0]][splits[1]] = 1
    
    total_rec = topN * user_count
    correct_rec = 0
    f = open(resultPath, 'r')
    result_data = f.readlines()
    for line in result_data:
        splits = line.split('|')
        if(user_dict[splits[0].strip()][splits[1].strip()] == 1):
            correct_rec += 1
    correct_ratio = correct_rec / total_rec
    print(str(correct_rec) + ' | ' + str(total_rec))
    print('correct ratio is : ' + str(correct_ratio))
    return correct_ratio;