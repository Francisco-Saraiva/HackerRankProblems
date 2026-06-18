# Easy Level Problem
# Note: MUST BE INTERPRETED IN PYTHON 2. Otherwise, hash() won't match their values

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(raw_input())  #raw_input is an analogous of input in python 2
    
    nums_tpl = tuple(map(int, raw_input().split()))
        
    print(hash(nums_tpl))