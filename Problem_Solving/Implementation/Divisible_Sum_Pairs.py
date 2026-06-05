#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#
#! Easy Level Problem

def divisibleSumPairs(n, k, ar):
    # Write your code here
    next_start = 0
    num_pairs = 0
    
    for j in range(next_start, n):
        for i in range(next_start+1, n):
            int_sum = ar[j] + ar[i]
            if int_sum % k == 0:
                num_pairs += 1
        next_start += 1
    
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
