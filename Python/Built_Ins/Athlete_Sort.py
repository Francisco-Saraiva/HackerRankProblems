# Medium Level Problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # sorted() preserves order in case of ties
    # Even if I had 3 conditions, in case of ties in all 3, it would preserve order
    sorted_arr = sorted(arr, key=lambda x: x[k])
    
    for row in sorted_arr:
        print(*row)
    
    
