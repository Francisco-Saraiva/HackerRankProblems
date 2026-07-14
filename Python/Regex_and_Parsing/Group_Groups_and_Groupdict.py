# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()

alphanumeric = "A-Za-z0-9"

pattern = fr"([{alphanumeric}])\1"

m = re.search(pattern, S)
if m:
    print(m.group(1))
else:
    print(-1)
