'''
Created on 2017年6月7日

@author: HotGaoGao
'''
first_dict = {}
second_dict = {}
count_0 = 1
while count_0 <= 5:
    count_1 = 1
    second_dict[str(count_0)] = dict()
#     while count_1 <= 5:
#         first_dict.setdefault(str(count_1), 0)
#         count_1 += 1
    while count_1 <= 5:
        second_dict[str(count_0)][str(count_1)] = 0
        count_1 += 1
#     second_dict.setdefault(str(count_0), first_dict)
    count_0 += 1
print(str(second_dict))
data = []
data.append('1,1')
data.append('2,2')
for line in data:
    splits = line.split(',')
    print(splits[0], splits[1])
    second_dict[splits[0]][splits[1]] = 1
print(str(second_dict))
