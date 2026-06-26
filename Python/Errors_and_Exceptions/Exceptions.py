# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    a, b = input().split(' ')
    
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
    except Exception as e:
        print("Error Code:", e)
        
