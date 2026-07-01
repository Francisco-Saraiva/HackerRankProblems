# Easy Level Problem
def wrapper(f):
    def fun(l):
        # complete the function
        for i, number in enumerate(l):
            num_len = len(number)
            
            if number.startswith("+91") and num_len > 10:
                l[i]= "+91 " + number[3:8] + " " + number[8:]
            elif number.startswith("91") and num_len > 10:
                l[i] = "+91 " + number[2:7] + " " + number[7:]
            elif number.startswith("0") and num_len > 10:
                l[i] = "+91 " + number[1:6] + " " + number[6:]
            elif len(number) == 10:  # If it's just a raw 10-digit number
                l[i] = "+91 " + number[0:5] + " " + number[5:]
        f(l)  # Calls sort phones
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


