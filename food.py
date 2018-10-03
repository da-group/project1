######################################
# Author: Jiachi Zhang
# email: zhangjiachi1007@gmail.com
######################################


import json


if __name__ == '__main__':

    f1 = open('./dataset/food-enforcement-0001-of-0001.json')
    f2 = open('./dataset/food-event-0001-of-0001.json')
    d1 = json.load(f1)
    d2 = json.load(f2)
    print(len(d1['results']))
    print(len(d2['results']))
    print(d1['results'][0])
    print(d2['results'][0])
