# Easy Level Problem

# namedtuples turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

N = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

avg = 0
for i in range(1, N+1):
    vals = input().split()
    new_std = Student(*vals)
    
    avg = ((avg * (i-1)) + int(new_std.MARKS)) / i

print(round(avg, 2))
    
