from numpy import linalg
import math

'''
Given data in the form data = [
                                [x1,x2,...xn],
                                [y1,y2,...yn]
                              ]

'''
length = 100

def matrixMultiply(A, v):
    if (len(v) != len(A[0])):
        return False
    output = []
    for i in range(len(A)):
        output.append(0)
        for j in range(len(A[i])):
            output[i] += A[i][j]*v[j]
    return output



def degree1(data):
    # Fit y = b + mx to the data

    A = [[1,data[0][0]]]
    for i in range(1,length):
        A.append([1,data[0][i]])
    # Calculate psuedoinverse by first getting Gram matrix (A^T)A
    norm = 0
    for i in range(0, length):
        norm+= math.pow(data[0][i],2)
    ATA = [
            [length, sum(data[0])],
            [sum(data[0]), norm]
          ]
    ATAinv = numpy.linalg.inv(ATA)
    inner = 0
    for i in range(0, length):
        inner += data[0][i]*data[1][i]
    ATyD = [
            [sum(data[1])],
            [inner]
           ]
    thetas = matrixMultiply(ATAinv, ATyD)
    # y = thetas[0] + thetas[1]*x
    return thetas

def degree2(data):
    # Fit y = ax^2 + bx + c to the data
    A = 1

def determine(data):
    degree = 1
    return degree
    # Check each of the polynomials, find the best
