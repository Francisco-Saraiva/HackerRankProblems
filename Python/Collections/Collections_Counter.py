# Easy Level Problem

# A Counter is a container that stores elements as dictionary keys,
# and their counts are stored as dictionary values.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split(' ')))
N = int(input())

shoe_counter = Counter(shoe_sizes)

money_earned = 0
for _ in range(N):
    shoe, price = map(int, input().split(' '))
    
    if shoe_counter[shoe] >= 1:
        shoe_counter[shoe] -= 1
        money_earned += price

print(money_earned)