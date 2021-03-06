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
    parser.add_argument('-f', type=str, default='./dataset/crime2017.csv', help='the file path')
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
        # The following line has a bug:
        # wrong_list = ~column.apply(lambda x: type(x)==column.dtype)
        # fixed by this:
        wrong_list = [type(column[i]) != column.dtype for i in column.index]
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
        # print(key, wrong_num)
        d[key] = cleanness

    # sort by cleaness
    sorted_list = sorted(d.items(), key=lambda ele: ele[1], reverse=True)
    return sorted_list


def main():
    args = getArguments()
    myData = pd.read_csv(args.f, sep=',', encoding='latin1')
    sorted_list = qualify(myData)
    print('the quality score of each attribute (the closer to 0, the cleaner the attribute):')
    for i in range(len(sorted_list)):
        print(sorted_list[i])


if __name__ == '__main__':
    main()

