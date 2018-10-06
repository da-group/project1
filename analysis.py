##########################################
# Author: Jiachi Zhang
# E-mail: zhangjiachi1007@gmail.com
##########################################

import argparse
import pandas as pd


def getArguments():
    '''
    get and parse command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='./dataset/crime2017.csv')
    return parser.parse_args()


def countNaN(column):
    '''
    count the missing value of a column
    '''
    NaN_list = column.isnull() # bool list indicate NaN
    NaN_num = sum(NaN_list)    # number of NaN
    return NaN_num, NaN_list


def values(column):
    '''
    statistic of column values
    '''
    values = pd.unique(column)
    num_values = len(values)
    frequency = column.value_counts()
    return frequency



def main():
    '''
    cleanness analysis
    '''
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    r_num, c_num = myData.shape
    for key in myData.columns:
        NaN_num, NaN_list = countNaN(myData[key])
        frequency = values(myData[key])
        print(key, NaN_num*1.0/r_num)
        print(frequency)




if __name__ == '__main__':
    main()
    '''
    myData = pd.read_csv('dataset/crime2017.csv', sep=',', encoding='latin1')
    print(myData.head())
    index = myData.isnull().any(axis=1)
    print(sum(index))
    print(myData.shape)
    '''

