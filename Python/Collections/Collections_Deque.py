# Easy Level Problem

# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

# Methods: pop(), popleft(), clear(), append(val), appendleft(val)
# extend(val_list), remove(val), reverse(), rotate(val)

N = int(input())
dq = deque()

for _ in range(N):
    cmd_parts = input().split(' ')
    cmd = cmd_parts[0]
    
    if cmd == "append":
        num = int(cmd_parts[1])
        dq.append(num)
        
    elif cmd == "pop":
        dq.pop()
        
    elif cmd == "popleft":
        dq.popleft()
        
    elif cmd == "appendleft":
        num = int(cmd_parts[1])
        dq.appendleft(num)

print(*dq)
    