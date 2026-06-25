# Medium Level Problem

# Enter your code here. Read input from STDIN. Print output to STDOUT4

from collections import deque

T = int(input())
dq = deque()

def solve_stacking(dq: deque) -> str:
    max_num = float('+inf')
    
    while dq:
        # Pop the largest value out of the ends
        if dq[0] > dq[-1]:
            val = dq.popleft()
        else:
            val = dq.pop()
        
        # Check if the value was smaller or equal to our current maximum
        # If not, then it is not solvable
        if val <= max_num:
            max_num = val
        else:
            return "No"
    
    return "Yes"
    
for _ in range(T):
    n = int(input())
    sideLengths = map(int, input().split(' '))
    dq = deque(sideLengths)
    print(solve_stacking(dq))
    