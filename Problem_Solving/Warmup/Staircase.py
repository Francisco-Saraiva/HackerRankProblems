#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
#! Easy Level Problem

def staircase(n):
    # Write your code here
    for i in range(1, n+1): # this way, the index tells me how many '#' I need
        num_spaces = n - i
        string = " " * num_spaces + "#" * i
        print(string)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
