#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
#! Easy Level Problem (somehow)

def gcd(num1, num2):
    remainder = -1
    
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp
    
    while True:
        remainder = num1 % num2
        if remainder == 0:
            break
        else:
            num1 = num2
            num2 = remainder
    
    return num2

def gcd_list(list_nums):
    result = list_nums[0]
    for n in list_nums[1:]:
        result = gcd(result, n)
    return result

def lcm(num1, num2):  # order is not important
    return int((num1*num2) / gcd(num1, num2))
    
def lcm_list(list_nums):
    result = list_nums[0]
    for n in list_nums[1:]:
        result = lcm(result, n)
    
    return result

def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)
    
    output = 0
    for candidate in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b % candidate == 0:
            output += 1
    
    return output
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
