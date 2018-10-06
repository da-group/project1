##########################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
##########################################

import argparse
import pandas as pd

from analysis import getArguments, countNaN


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


def dropRows(myData):
    '''
    drop rows with NaN values
    '''
    boollist = myData.isnull().any(axis=1)
    return myData[~boollist]


def clean():
    '''
    clean the data
    '''
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    print(myData.shape)
    myData = dropColumns(myData, 0.1)
    myData = dropRows(myData)
    print(myData.shape)


if __name__ == '__main__':
    main()


