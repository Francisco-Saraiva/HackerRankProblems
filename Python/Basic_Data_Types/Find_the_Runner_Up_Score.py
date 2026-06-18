# Easy Level Problem

# Solution 1: more readable and O(nlogn)
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    
#     list_arr = list(set(arr))
    
#     list_arr.sort(reverse=True)
    
#     print(list_arr[1])
    
# Solution 2: a bit more complex, O(n) [single pass]
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Low values, problem specifications
    winner = -101
    runner_up = -101
    
    for score in arr:
        if score > winner:
            runner_up = winner  # The old runner up is now a winner
            winner = score
        elif score < winner and score > runner_up:
            runner_up = score
    print(runner_up)
    
    
    