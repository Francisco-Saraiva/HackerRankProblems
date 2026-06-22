# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Set A
_ = input()
set_A = set(map(int, input().split(' ')))

# Operation Pairs
N = int(input())

for _ in range(N):
    cmd = input().split(' ')[0]
    op_set = set(map(int, input().split(' ')))
    
    if cmd == "update":
        set_A |= op_set
        
    elif cmd == "intersection_update":
        set_A &= op_set
        
    elif cmd == "difference_update":
        set_A -= op_set
        
    elif cmd == "symmetric_difference_update":
        set_A ^= op_set
        
print(sum(set_A))

