# Medium Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

S = input()

groups = []
uniquekeys = []
pairs = []

for k, g in groupby(S):
    group = list(g)
    pairs.append((len(group), int(k)))
    
print(*pairs)