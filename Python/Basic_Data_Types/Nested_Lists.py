# Easy Level Problem

if __name__ == '__main__':
    
    loser_list = []
    runner_up_list = []
    
    loser = float('+inf')
    runner_up = float('+inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score < loser:
            runner_up_list = list(loser_list) # independent copy from the loser_list
            loser_list = [name]
            
            runner_up = loser
            loser = score
            
        elif score == loser:
            loser_list.append(name)
            
        elif score < runner_up and score > loser:
            runner_up = score
            runner_up_list = [name]
            
        elif score == runner_up:
            runner_up_list.append(name)
    
    runner_up_list.sort()
    for name in runner_up_list:
        print(name)
    
    
        
        
                