# Medium Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

o_dict = OrderedDict()

for _ in range(n):
    word = input()
    
    if word not in o_dict:
        o_dict[word] = 1
    else:
        o_dict[word] += 1

print(len(o_dict))
print(*o_dict.values())