#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
#! Easy Level Problem

def breakingRecords(scores):
    # Write your code here
    lowest_score = 1_000_000_001
    highest_score = -1
    records_broken = [-1,-1] # Start at -1 because the 1st score will automatically update both up to 0, and start the "regular cycle"
    
    for score in scores:
        if score < lowest_score:
            lowest_score = score
            records_broken[1] += 1
        
        if score > highest_score:
            highest_score = score
            records_broken[0] += 1
    
    return records_broken

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
