##########################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
##########################################

import argparse
import pandas as pd

from analysis import getArguments, countNaN, wrongValues, qualify


def dropColumns(myData, thre, sorted_list):
    '''
    drop columns whose (NaN + wrong)/(row numbers) > thre
    '''
    for key, value in sorted_list:
        if value > thre:
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
    # evaluate
    sorted_list = qualify(myData)
    print(sorted_list)
    # drop columns
    myData = dropColumns(myData, 0.1, sorted_list)
    sorted_list = qualify(myData)
    # drop rows
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


