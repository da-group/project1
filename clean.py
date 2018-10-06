##########################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
##########################################

import argparse
import pandas as pd

from analysis import getArguments, countNaN, wrongValues, qualify


def dropColumns(myData, thre):
    '''
    drop columns whose (NaN number)/(row numbers) > thre
    '''
    N, C = myData.shape
    for key in myData.columns:
        NaN_num, NaN_list = countNaN(myData[key])
        if (NaN_num)*1.0/N > thre:
            myData = myData.drop(key, axis=1)
    return myData


def dropRows(myData, column):
    '''
    drop rows with NaN values
    '''
    _, NaN_l = countNaN(column)
    _, wrong_l = wrongValues(column)
    return myData[~(NaN_l|wrong_l)]


def clean(myData):
    '''
    clean the data
    '''
    myData = dropColumns(myData, 0.1)
    sorted_list = qualify(myData)
    print(sorted_list)
    for i in range(3):
        myData = dropRows(myData, myData[sorted_list[i][0]])
    sorted_list = qualify(myData)
    print('after clean')
    print(sorted_list)


def main():
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    clean(myData)


if __name__ == '__main__':
    main()


