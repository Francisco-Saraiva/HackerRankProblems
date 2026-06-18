# Easy Level Problem

# Solution 1: use a method that already does that
# def swap_case(s):
#     return s.swapcase()

# Solution 2: without said method, kinda defeats the purpose
def swap_case(s):
    new_str = ""
    for char in s:
        if char.isupper():
            new_str = new_str + char.lower()
        elif char.islower():
            new_str = new_str + char.upper()
        else:
            new_str = new_str + char
    
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)