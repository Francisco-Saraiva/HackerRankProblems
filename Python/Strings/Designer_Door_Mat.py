# Easy Level Problem

# Read the input values
size = list(map(int, input().split()))
N = size[0] # Number of rows (mat height)
M = size[1] # Number of columns (mat width)

loop_num = N // 2
num_dashes = (M-3) // 2 
num_dingus = 1

list_strs = [""] * loop_num

# Create and store the mat's rows, to use later
for i in range(loop_num):
    pattern = ".|."
    list_strs[i] = "-"*num_dashes + pattern*num_dingus + "-"*num_dashes
    num_dashes -= 3
    num_dingus += 2

# Create the welcome part of the mat
welcome_str = "-"*((M-7)//2) + "WELCOME" + "-"*((M-7)//2)

# Print the mat
# Top part
for row in list_strs:
    print(row)

# Welcome part
print(welcome_str)

# Bottom part
for row in list_strs[::-1]:
    print(row)
    