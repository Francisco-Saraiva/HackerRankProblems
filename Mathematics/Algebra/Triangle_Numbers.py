#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
#! Medium Level Problem

def solve(n):
    # Write your code here
    if n % 2 == 1:
        out = 2
    elif n % 4 == 0:
        out = 3
    elif n % 2 == 0:
        out = 4
    else:
        out = -1
            
    return out
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
