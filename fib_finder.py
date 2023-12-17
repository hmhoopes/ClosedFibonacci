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
    
    vals = [0 for i in range(index+1)]
    vals[1] = 1
    for i in range(2, index+1):
        vals[i] = vals[i-1] + vals[i-2]
    return vals[-1]
