#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
#! Easy Level Problems

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    # Add d + tree position
    apple_pos = [apple + a for apple in apples]
    orange_pos = [orange + b for orange in oranges]
    
    count = [0,0]  # apples/oranges
    
    # We need 2 separate loops since m is not equal to n [first approach]
    # for i in range(len(apple_pos)):
    #     if apple_pos[i] >= s and apple_pos[i] <= t:
    #         count[0] += 1
            
    # for j in range(len(orange_pos)):
    #     if orange_pos[j] >= s and orange_pos[j] <= t:
    #         count[1] += 1
    m = len(apple_pos)
    n = len(orange_pos)
    
    max_loop_idx = m if m > n else n
    
    for i in range(max_loop_idx):
        if i < m:  
            if apple_pos[i] >= s and apple_pos[i] <= t:
                count[0] += 1
        if i < n:
            if orange_pos[i] >= s and orange_pos[i] <= t:
                count[1] += 1
    
    print(count[0])
    print(count[1])
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
