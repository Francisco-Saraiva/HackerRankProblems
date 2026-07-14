# Easy Level Problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

N = int(input())

pattern = r"^[789][0-9]{9}$"

for _ in range(N):
    phone_num = input()
    m = re.search(pattern, phone_num)
    
    if m:
        print("YES")
    else:
        print("NO")