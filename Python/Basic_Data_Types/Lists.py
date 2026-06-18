# Easy Level Problem

if __name__ == '__main__':
    N = int(input())
    
    num_list = []
    
    for _ in range(N):
        cmd_parts = input().split()
        command = cmd_parts[0]
        
        if command == "insert":
            pos = int(cmd_parts[1])
            integer = int(cmd_parts[2])
            num_list.insert(pos, integer)
            
        elif command == "print":
            print(num_list)
            
        elif command == "remove":
            integer = int(cmd_parts[1])
            num_list.remove(integer)
            
        elif command == "append":
            integer = int(cmd_parts[1])
            num_list.append(integer)
            
        elif command == "sort":
            num_list.sort()
            
        elif command == "pop": 
            num_list.pop()
               
        elif command == "reverse": 
            num_list.reverse() 
             