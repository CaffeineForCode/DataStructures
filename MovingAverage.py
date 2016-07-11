'''
Project Name : MovingAverage
Created By : Mrigank
Date : 6/11/16
Purpose : to find the moving average in an array for given window size
'''

import numpy as np
#given dataset
dataset = [10, -1, 3, 7, 2, 0, 10, 1, 5, 9, 2, 4, 7, -10]


def findMovineAvg(data, windowSize):
    weight = np.repeat(1.0, windowSize)/windowSize
    avg = np.convolve(data, weight, 'valid')
    return avg

if __name__ == '__main__':
    print(findMovineAvg(dataset,3))