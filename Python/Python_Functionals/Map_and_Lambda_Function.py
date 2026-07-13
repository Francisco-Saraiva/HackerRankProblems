# Easy Level Problem

cube = lambda x: pow(x,3)# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    # Edge cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    # For n >= 2
    prev_2 = 0
    prev_1 = 1
    fib_list = [0, 1]
    
    for i in range(2, n):
        # Calculate the next fibonacci number
        curr = prev_2 + prev_1
        fib_list.append(curr)
        
        # Update previous numbers
        prev_2 = prev_1
        prev_1 = curr
    
    return fib_list
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))