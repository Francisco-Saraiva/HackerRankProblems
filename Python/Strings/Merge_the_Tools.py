# Medium Level Problem
# Solution 1: My solution
def merge_the_tools(string, k):
    # your code goes here
    
    n = len(string)
    list_strs = []
    set_strs = set()
    
    for i in range(int(n/k)):
        curr_str = ""
        for j in range(k):
            char = string[k*i + j]
            if char not in set_strs:
                set_strs.add(char)
                curr_str += char
        
        list_strs.append(curr_str)
        set_strs.clear()
        curr_str = ""
        
    for substr in list_strs:
        print(substr)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Solution 2: Optimized for python
def merge_the_tools(string, k):
    # Loop through the string in steps of k
    for i in range(0, len(string), k):
        # Slice out the current chunk of size k
        chunk = string[i : i + k]
        
        # dict.fromkeys() removes duplicates while keeping character order perfectly.
        # ''.join() stitches the unique keys back into a string.
        print(''.join(dict.fromkeys(chunk)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)