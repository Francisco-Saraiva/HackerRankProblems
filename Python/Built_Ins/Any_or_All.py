# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
num_list = input().strip().split()

cond1 = all(int(num) > 0 for num in num_list)
cond2 = False

if cond1: # only check condition 2 in case 1 was true to save time
    cond2 = any(int(num) == int(num[::-1]) for num in num_list)
    
print(cond2)
