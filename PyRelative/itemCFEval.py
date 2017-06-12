'''
Created on 2017年6月6日

@author: HotGaoGao
'''
def doEvaluate(topN, user_count):
    f = open('../ml-100k/u1.test', 'r')
    data = f.readlines()
    f.close()
    user_dict = dict()
    rating_dict = dict()
    count_0 = 1
    # ff = open('test_dict.txt', 'w')
    while count_0 <= 943:
        count_1 = 1
        user_dict[str(count_0)] = dict()
        while count_1 <= 1682:
            user_dict[str(count_0)][str(count_1)] = 0
    #         rating_dict.setdefault(str(count_1), 0)
            count_1 += 1
    #     user_dict.setdefault(str(count_0), rating_dict)
        count_0 += 1
    # ff.write(str(user_dict))
    # ff.write('\n')
    # print(user_dict)
    
    for line in data:
        splits = line.split('\t')
    #     print(line)
        user_dict[splits[0]][splits[1]] = 1
    # print(user_dict)
    
    # ff.write(str(user_dict))
    
    total_rec = topN * user_count
    correct_rec = 0
    f = open('result.txt', 'r')
    test_data = f.readlines()
    for line in test_data:
        splits = line.split('|')
    #     print(splits)
        if(user_dict[splits[0].strip()][splits[1].strip()] == 1):
#             print(splits[0], splits[1])
            correct_rec += 1
    correct_ratio = correct_rec / total_rec
    print('correct ratio is : ' + str(correct_ratio))