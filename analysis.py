##########################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
##########################################


import pandas as pd

if __name__ == '__main__':
    myData = pd.read_csv('dataset/crime2017.csv', sep=',', encoding='latin1')
    print(myData.head())
    index = myData.isnull().any(axis=1)
    print(sum(index))
    print(myData.shape)

