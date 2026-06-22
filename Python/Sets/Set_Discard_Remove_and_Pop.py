# Easy Level Problem

n = int(input())
s = set(map(int, input().split()))

# Commands: pop, remove, discard
N = int(input())

for _ in range(N):
    cmd_parts = input().split(' ')
    instruction = cmd_parts[0]
    
    if instruction == "pop":
        s.pop()
        
    elif instruction == "remove":
        num = int(cmd_parts[1])
        s.remove(num)
        
    elif instruction == "discard":
        num = int(cmd_parts[1])
        s.discard(num)

print(sum(s))