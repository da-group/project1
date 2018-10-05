######################################
# Author: Jiachi Zhang
# email: zhangjiachi1007@gmail.com
######################################


import json


if __name__ == '__main__':

    f1 = open('./dataset/food-enforcement-0001-of-0001.json')
    f2 = open('./dataset/food-event-0001-of-0001.json')
    f3 = open('./dataset/drug-event-0002-of-0004.json')
    d1 = json.load(f1)
    d2 = json.load(f2)
    d3 = json.load(f3)
    '''
    print(len(d1['results']))
    print(len(d2['results']))
    print(len(d3['results']))
    print(d1['results'][0])
    print(d2['results'][0])
    print(d3['results'][0])
    '''
    for i in range(5):
        print(d2['results'][i])
