######################################
# Author: Jiachi Zhang
# email: zhangjiachi1007@gmail.com
######################################


import json


with open('./dataset/food-enforcement-0001-of-0001.json') as f:
    d = json.load(f)
    print(type(d))
    print(d.keys())
    print(type(d['results']))
    print(len(d['results']))
    print(d['results'][0])

