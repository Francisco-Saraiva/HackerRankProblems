# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split(' ')

S = sorted(S) # If the input is sorted, so will the permutations
k = int(k)

permuts = list(permutations(S, k))

for p in permuts:
    print(''.join(p))
