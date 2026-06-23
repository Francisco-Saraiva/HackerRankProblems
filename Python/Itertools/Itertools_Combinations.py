# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = input().split(' ')

S = sorted(S) # If the input is sorted, so will the permutations
k = int(k)

comb_list = []

for i in range(1, k+1):
    comb_list.extend(list(combinations(S,i)))

for c in comb_list:
    print(''.join(c))