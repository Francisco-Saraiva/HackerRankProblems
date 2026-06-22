# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1: Using sets

K = int(input())
room_nums = list(map(int, input().split(' ')))

set_unique = set()
room_dupes = set()

for room in room_nums:
    if (room not in set_unique) and (room not in room_dupes):
        set_unique.add(room)
        
    elif (room in set_unique) and (room not in room_dupes):
        set_unique.discard(room)
        room_dupes.add(room)

print(set_unique.pop())

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 2: Clever way

K = int(input())
room_nums = list(map(int, input().split(' ')))
unique_rooms = set(room_nums)

# Sum all the room numbers
room_sum = sum(room_nums)

# What if there were K captains? What would the value of their sum be?
imag_room_sum = sum(unique_rooms) * K

# Calculate the SUM(value(K-1 captains))
sum_k_minus_1_capts = imag_room_sum - room_sum

# Divide by K-1 to get the value of the captain
captain_room = sum_k_minus_1_capts // (K-1)

print(captain_room)

