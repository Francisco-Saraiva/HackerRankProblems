# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Set 1
_ = input()
set1 = set(map(int, input().split()))
# Set 2
_ = int(input())
set2 = set(map(int, input().split()))

# Compute the symmetric difference
sym_diff = set1 ^ set2

for el in sorted(sym_diff):
    print(el)