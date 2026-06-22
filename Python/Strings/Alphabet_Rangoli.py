# Easy Level Problem

def print_rangoli(size):
    # your code goes here
    
    # Calculate the number of outer dashes we need
    line_width = (size-1)*4 + 1
    half_line = (line_width // 2) + 1
    num_dashes = half_line - 1
    
    # Prepare to store each line. 
    # Calculate all letters until size, and reverse
    list_strs = [""] * size
    list_letters = [chr(ord('`') + k) for k in range(1, size + 1)][::-1]
        
    for l in range(size):
        line = "-"*num_dashes # Always start with the  outer dashes
        for i in range(l+1):
            if i == l:
                line += list_letters[i] # if it is not the middle letter
            else:
                line += list_letters[i] + "-" # if it is the middle letter
        list_strs[l] = line + line[:-1][::-1]  # cut middle letter, reverse and append
        num_dashes -= 2
    
    # Print out the pattern
    for row in list_strs:
        print(row)
    
    for row in list_strs[:-1][::-1]:
        print(row)
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)