# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()

consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
vowels = "AEIOUaeiou\+\-"

pattern = fr"(?<=[{consonants}])[{vowels}]{{2,}}(?=[{consonants}])"

substrs = re.findall(pattern, S)

if substrs:
    for m in substrs:
        print(m)
else:
    print(-1)