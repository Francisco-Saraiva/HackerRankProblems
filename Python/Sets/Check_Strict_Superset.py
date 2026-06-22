# Easy Level Problem
# Solution 1
# Enter your code here. Read input from STDIN. Print output to STDOUT

# set_A = set(map(int, input().split(' ')))

# n = int(input())

# is_superset = True
# counter = 0

# while is_superset and counter < n:
#     comparison_set = set(map(int, input().split(' ')))
    
#     is_superset = (set_A > comparison_set)
    
#     counter += 1

# print(is_superset)

# Solution 2: Ultra Pythonic
set_A = set(map(int, input().split()))
n = int(input())

# Check if set_A is a strict superset for ALL incoming input sets
result = all(set_A > set(map(int, input().split())) for _ in range(n))

print(result)