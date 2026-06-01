#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#! Easy Level Problem

def plusMinus(arr):
    # Write your code here
    # How many numbers are there
    total = len(arr)
    
    # Number of zeros
    zeros = arr.count(0)
    
    # Number of positives
    positives = sum(1 for val in arr if val>0)
    
    # Number of negatives
    negatives = total - positives - zeros
    
    # Fractions
    frac_zeros = round(zeros/total, 6)
    frac_positives = round(positives/total, 6)
    frac_negatives = round(negatives/total, 6)
    
    # Prints
    print(frac_positives)
    print(frac_negatives)
    print(frac_zeros)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
