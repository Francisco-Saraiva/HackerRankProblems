# Hard Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

K, M = map(int, input().split(' '))

num_lists = []
for _ in range(K):
    nums = list(map(int, input().split(' ')))
    length = nums[0]
    num_lists.append(nums[1:])


all_combinations = list(product(*num_lists))
results = [(sum(num**2 for num in tpl) % M) for tpl in all_combinations]

print(max(results))