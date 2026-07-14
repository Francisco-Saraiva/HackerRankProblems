# Easy Level Problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

T = int(input())

upper_pattern = r"[A-Z]"
digit_pattern = r"[0-9]"

for _ in range(T):
    uid = input()
    
    char_set = set(uid)
    
    upper_matches = re.findall(upper_pattern, uid)
    digit_matches = re.findall(digit_pattern, uid)
    
    if len(upper_matches) >= 2 and len(digit_matches) >= 3 and uid.isalnum and len(uid) == 10 and len(char_set) == 10:
        print("Valid")
    else:
        print("Invalid")
    
    