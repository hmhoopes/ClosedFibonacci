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

def closed_form(index):
    M = np.mat(np.array([[0,1],[1,1]]))
    #Creates matrix for M
    eigvals, P = np.linalg.eig(M)
    #Stores eigen vectors in P
    D = np.mat(np.array([[eigvals[0]**index, 0], [0, eigvals[1]**index]]))
    #Transforms eigen values to form necessitated by D
    Pinv = np.linalg.inv(P)
    #Store P inverse
    PDPinv = np.matmul(np.matmul(P, D), Pinv)
    #Gets PD^kP^-1
    return PDPinv[0, 1]
    #Because x0 = 0 and x1 = 1, matrix-vector multiplication would return the element in row 0, column 1
