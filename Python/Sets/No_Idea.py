# Medium Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split(' '))

list_nums = list(map(int, input().split(' ')))

happy_set = set(map(int, input().split(' ')))
sad_set = set(map(int, input().split(' ')))

happiness = 0
for num in list_nums:
    if num in happy_set:
        happiness += 1
    elif num in sad_set:
        happiness -= 1

print(happiness)
    
