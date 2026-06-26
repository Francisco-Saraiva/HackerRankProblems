# Easy Level Problem
# Must be on Python 2!
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

for _ in range(T):
    regexp = raw_input()
    try:
        re.compile(regexp)
        print("True")
    except re.error:
        print("False")
