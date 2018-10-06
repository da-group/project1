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


def wrongValues(column):
    '''
    count wrong values whose data type is incompatible
    '''
    # First, drop the NaN rows
    _, NaN_list = countNaN(column)
    column = column[~NaN_list]
    # when the variable type is str
    if column.dtype==object:
        wrong_list = ~column.apply(lambda x: isinstance(x, str))
        wrong_num = sum(wrong_list)
        return wrong_num, wrong_list
    # when the data type is numerical (int, float and so on)
    else:
        wrong_list = ~column.apply(lambda x: type(x)==column.dtype)
        wrong_num = sum(wrong_list)
        return wrong_num, wrong_list



def qualify(myData):
    '''
    cleanness analysis
    try to qualify the cleanness of attributes
    the lower the value is, the less clean the attribute is
    '''
    r_num, c_num = myData.shape
    # define key-cleanness quality dictionary
    d = {}
    for key in myData.columns:
        NaN_num, NaN_list = countNaN(myData[key])
        wrong_num, wrong_list = wrongValues(myData[key])
        # cleanness is defined by ratio of bad values and NaN values
        cleanness = (NaN_num+wrong_num)*1.0/r_num
        d[key] = cleanness

    # sort by cleaness
    sorted_list = sorted(d.items(), key=lambda ele: ele[1], reverse=True)
    return sorted_list


def main():
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    sorted_list = qualify()
    print('find 3 Least clean attributes are:')
    for i in range(3):
        print(sorted_list[i])


if __name__ == '__main__':
    main()

