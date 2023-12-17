import numpy as np 
def rec_finder(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return rec_finder(index-1) + rec_finder(index-2)

def iterative_finder(index):
    if index == 0:
        return 0
    first = 1
    second = 0
    for i in range(1, index):
        temp = first
        first += second
        second = temp
    return first
