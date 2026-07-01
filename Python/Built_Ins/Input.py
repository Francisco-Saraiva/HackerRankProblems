# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())

polynomial = input()
poly_func = lambda x: eval(polynomial)

val = poly_func(x)

print(True if val == k else False)
