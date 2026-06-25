# Easy Level Problem
# DefaultDict: You don't need to check if a key exists to add a new element

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split(' '))

# Initialize the dictionaries. Inside the parenthesis, specify the datatype
# that each key will hold; could be int, set, tuple, ...
d_A = defaultdict(list)

for i in range(n):
    d_A[input()].append(i+1)

# We don't actually need to create the 2nd one. We can just print out the value immediately
for j in range(m):
    word = input()
    # Unpack operator (*) will try to unpack -1. Put it in a list
    print(*d_A[word] if word in d_A else [-1])
    #print(*d_A.get(word, [-1]))  # Better syntax alternative