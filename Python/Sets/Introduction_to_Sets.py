# Easy Level Problem

def average(array):
    # your code goes here
    set_heights = set(array)
    return sum(set_heights) / len(set_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)