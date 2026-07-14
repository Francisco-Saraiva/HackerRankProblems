# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

str_len = len(S)
pat_len = len(k)

match_set = set()

offset = 0

m = re.search(k, S)
while m and str_len >= pat_len:
    
    match_set.add((m.start() + offset, m.end() - 1 + offset))
    
    S = S[1:]
    
    str_len -= 1
    offset += 1
    m = re.search(k, S)

pair_list = sorted(list(match_set))

if not(pair_list):
    print((-1, -1))
    
else:
    for pair in pair_list:
        print(pair)

# # Cleaned up version
# import re

# S = input()
# k = input()

# # Compile the pattern so we can use the 'pos' argument in search()
# pattern = re.compile(k)

# pair_list = []
# start_pos = 0

# # Search starting at start_pos
# m = pattern.search(S, pos=start_pos)

# while m:
#     # 1. Grab the start and end (inclusive) indices
#     pair_list.append((m.start(), m.end() - 1))
    
#     # 2. Advance the search window by exactly 1 to handle overlaps
#     start_pos = m.start() + 1
    
#     # 3. Search again starting from the new position
#     m = pattern.search(S, pos=start_pos)

# # Print the results
# if not pair_list:
#     print((-1, -1))
# else:
#     for pair in pair_list:
#         print(pair)