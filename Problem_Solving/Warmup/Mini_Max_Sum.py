#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#! Easy Level Problem
def miniMaxSum(arr):
    # Write your code here
    min_val = min(arr)
    max_val = max(arr)
    
    max_sum = sum(arr) - min_val
    min_sum = sum(arr) - max_val
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
