# Easy Level Problem

# Solution 1 : My way of thinking, char by char. Would be ever so
# slightly faster with 5 different variables

# if __name__ == '__main__':
#     s = input()
    
#     # alphanumeric, alpabetical, digits, lowercase, uppercase
#     check_list = [False] * 5
    
#     for char in s:
#         if char.isalpha():
#             check_list[0] = True
#             check_list[1] = True
            
#         elif char.isdigit():
#             check_list[0] = True
#             check_list[2] = True
            
#         if char.islower():  # A character can be alpha AND lower
#             check_list[3] = True
            
#         elif char.isupper():
#             check_list[4] = True
        
#         if all(check_list):
#             break
    
#     for check in check_list:
#         print(check)

# Solution 2: "Ultra Pythonic" way
if __name__ == '__main__':
    s = input()
    
    # any() has early stopping already implemented in it. So it is just as fast
    # if not faster then going step by step
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))