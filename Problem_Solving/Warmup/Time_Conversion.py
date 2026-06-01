#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
#! Easy Level Problem

def timeConversion(s):
    # Write your code here
    
    # Get the various parts of the string
    str_len = len(s)
    hour = int(s[0:2])
    time_of_day = s[str_len-2:str_len]
    rest = s[2:str_len-2]
    
    # Change the hour depending on time of day
    if (time_of_day == "PM" and hour != 12):
        hour += 12
    elif (time_of_day == "AM" and hour == 12): # edge case
        hour = 0
        
    # Return the new string
    hour_str = "0"+str(hour) if hour < 10 else str(hour) #add leading zero back
    return hour_str + rest
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
