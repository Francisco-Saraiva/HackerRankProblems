# Medium Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1: My thought process. Divide and join back

line = input()

lower_line = [char for char in line if char.islower()]
upper_line = [char for char in line if char.isupper()]
digit_line = map(int, [char for char in line if char.isdigit()])

lower_line = ''.join(sorted(lower_line))
upper_line = ''.join(sorted(upper_line))

digit_line = sorted(digit_line, key=lambda x: (x % 2 == 0, x))
digits_str = ''.join(map(str, digit_line))

out_str = lower_line + upper_line + digits_str
print(out_str)

# Solution 2: 1-liner
# Conditions go "backwards". FALSES will be at the FRONT, TRUES in the BACK
# As such the logic is the following:
# 1- place digits back
# 2- tiebreaker between digits
# 3- place uppers back (after already having placed digits in the back)
# 4- remaining letters at the front (so, only lowers). Also serves as a tiebreaker to sort alphabetically/numerically
print(*sorted(input(), key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c)), sep='')