# Medium Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

N = int(input())
chars = input().replace(" ", "")
K = int(input())

comb_list = list(combinations(chars, K))

total_cases = len(comb_list)
# The "in" operator works in tuples as well (any iterable in fact)
favourable_cases = sum(1 for string in comb_list if "a" in string)

print(favourable_cases / total_cases)

