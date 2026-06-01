#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
#! Medium Level Problem

def formingMagicSquare(s):
    # Write your code here
    
    NUM_MAGICS = 8 # number of magic squares
    NUM_ELEMENTS = 9 # number of elements in each matrix/magic square
    
    costs = [0] * NUM_MAGICS
    
    magics = [
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    
    # Linearize input for easier processing
    s_linear = []
    for row in s:
        for element in row:
            s_linear.append(element)
    
    # Calculate cost for every magic square 
    #(can be optimized to stop once I found a cost = 0 AND stop mid-loop when cost > min_cost)
    cost_per_element = [0] * NUM_ELEMENTS
    for m, magic in enumerate(magics):
        for i in range(NUM_ELEMENTS):
            cost_per_element[i] = abs(magic[i] - s_linear[i])
        costs[m] = sum(cost_per_element)
    
    return min(costs)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
