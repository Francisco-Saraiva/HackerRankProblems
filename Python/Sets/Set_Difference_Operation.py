# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Set 1
_ = input()
set1 = set(map(int, input().split(' ')))

# Set 2
_ = input()
set2 = set(map(int, input().split(' ')))

difference_set = set1 - set2
print(len(difference_set))