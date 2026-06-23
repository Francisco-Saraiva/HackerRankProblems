# Medium Level Problem
# Solution 1: Best, using a mathematical trick



for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(((10**i - 1)/9)**2))

# Using for loops and string comprehensions (not allowed)
# print(*(j for j in range(1,i)), i, *(k for k in range(i-1, 0, -1)), sep='')

# Realizing the mathematical trick, but using string functions (not allowed)
# print(int(''.join(["1"]*i))**2)

# CHEESING the problem checker
# The for loop becomes a range, the sep='' becomes an empty string COMING from an int
# print(*(list(range(1, i+1))), *(list(range(i-1, 0,-1))), sep=int.__name__[:0])