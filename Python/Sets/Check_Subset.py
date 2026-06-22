# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for _ in range(T):
    dummy = input()
    set_A = set(map(int, input().split(' ')))
    
    dummy = input()
    set_B = set(map(int, input().split(' ')))
    
    print(set_A <= set_B)