# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr

S, k = input().split(' ')

S = sorted(S) # If the input is sorted, so will the permutations
k = int(k)

combs_rep = list(cwr(S,k))

for c in combs_rep:
    print(''.join(c))