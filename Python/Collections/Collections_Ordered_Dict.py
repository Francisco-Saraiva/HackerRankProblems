# Easy Level Problem

# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

item_dict = OrderedDict()

N = int(input())

for _ in range(N):
    inputs = input().split(' ')
    
    price = int(inputs[-1])
    item = ' '.join(inputs[:-1])
    
    if item not in item_dict:
        item_dict[item] = price
    else:
        item_dict[item] += price

for key in item_dict.keys():
    print(key, item_dict[key])
    
    