import numpy as np
from numpy import linalg
import math
import plotly.plotly as py
import plotly.graph_objs as go

# N = 1000
# random_x = np.random.randn(N)
# random_y = np.random.randn(N)
#
# # Create a trace
# trace = go.Scatter(
#     x = random_x,
#     y = random_y,
#     mode = 'markers'
# )
#
# data = [trace]
#
# # Plot and embed in ipython notebook!
# py.iplot(data, filename='basic-scatter')
#
'''
Given data in the form data = [
                                [x1,x2,...xn],
                                [y1,y2,...yn]
                              ]
Fix scatter plot library
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
    # This function is computationally efficient for least squares soln.
    A = [
            [1,data[0][0]]
        ]
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
    # Fit y = thetas[0] + thetas[1]*x + thetas[2]*x^2 to the data
    A = 1

def degreeN(data, n):
    # Fit a degree n polynomial to the data y = thetas[0] + ... + thetas[n]*x^n
    initial = [1, data[0][0]]
    for i in range (2, n):
        initial.append(math.pow(data[0][0],i))
    A = [
            initial
        ]
    for i in range(1, n):
        set = [1, data[0][i]]
        for j in range(2, n):
            set.append(math.pow(data[0][i],j))
        A.append(set)
    # We have created a Vandermonde matrix here
    # To calculate A_dagger*y^d, it will be computationally inefficient
    # so that it can be generalized up to 20 degrees
    A_dag = numpy.matmul(numpy.linalg.inv(numply.matmul(numpy.matrix.transpose(A),A)),numpy.matrix.transpose(A))
    y_d = data[1]
    thetas = matrixMultiply(A_dag, y_d)
    return thetas

def predError(thetas, data):
    # Use RMS Prediction error to determine the accuracy of a polynomial

def determine(data):
    # Check each of the polynomials, find the best
    for i in range(1,12):

    return degree
