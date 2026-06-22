# Easy Level Problem

def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        d = str(i).rjust(width)
        o = oct(i)[2:].rjust(width)
        h = hex(i)[2:].rjust(width).upper()
        b = bin(i)[2:].rjust(width)
        
        print(d, o, h, b)
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)