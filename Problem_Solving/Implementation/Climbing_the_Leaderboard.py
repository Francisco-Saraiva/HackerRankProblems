#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
#! Medium Level Problem

def climbingLeaderboard(ranked, player):
    # Write your code here
    # Remove duplicates for easier ranking
    ranked_mod = list(set(ranked))
    ranked_mod.sort(reverse=True)
    
    # Get the number of players and ranked scores
    num_players = len(player)
    num_scores = len(ranked_mod)
    
    # Output list
    output = [0] * num_players
        
    idx_p = 0  # index to go through player scores
    idx_r = num_scores - 1 # index to go through ranked leaderboard scores
    
    while idx_p < num_players:
        print(idx_r)
        # If I went through the whole leaderboard
        if idx_r == -1:
            output[idx_p] = 1
            idx_p += 1
            continue
        
        if player[idx_p] < ranked_mod[idx_r]:
            output[idx_p] = idx_r + 2
            idx_p += 1
        else: # larger or equal
            idx_r -= 1
        
    
    return output
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
