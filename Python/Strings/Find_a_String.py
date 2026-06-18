# Easy Level Problem

def count_substring(string, sub_string):
    window_size = len(sub_string)
    str_len = len(string)
    
    counter = 0
    for i in range(str_len - window_size + 1):
        curr_str = string[i:i+window_size]
        if curr_str == sub_string:
            counter += 1
    
    return counter
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)