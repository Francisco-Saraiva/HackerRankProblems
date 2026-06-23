# Medium Level Problem
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    # Format layout: Day Name, Day Month Year Hour:Minute:Second Timezone
    time_format = "%a %d %b %Y %H:%M:%S %z"

    # Automatically convert strings to datetime objects
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)

    # 2. Subtract them to get a timedelta object, then pull total seconds as an integer
    return str(int(abs((dt1 - dt2).total_seconds())))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# My attempt at doing this manually

# import math
# import os
# import random
# import re
# import sys

# from datetime import datetime
# import calendar


# # Complete the time_delta function below.
# def time_delta(t1, t2):
    
#     # Time differences
#     td_t1 = t1[-5:]
#     td_t2 = t2[-5:]
    
#     # Remove day name and time differences
#     t1 = t1[4:-6]
#     t2 = t2[4:-6]
    
#     # Separate each attribute
#     t1_att = t1.split(' ')
#     t2_att = t2.split(' ')
    
#     # Convert the month name into a number
#     t1_att[1] = list(calendar.month_name).index(t1_att[1])
#     t2_att[1] = list(calendar.month_name).index(t2_att[1])
    
#     # Separate hour/minute/second from timestamp
#     t1_att.extend(t1_att[3].split(':'))
#     t1_att.pop(3)
    
#     t2_att.extend(t2_att[3].split(':'))
#     t2_att.pop(3)
    
#     # Convert all elements into integers
#     t1_att = list(map(int, t1_att))
#     t2_att = list(map(int, t2_att))
    
#     # Calculate the differences
#     result = [0] * 6
#     for i in range(6):
#         result[i] = t1_att[i] - t2_att[i]
    
#     # Convert time differences to seconds
#     diff_time = result[0] * 86400 \
#         + result[1] * 2_592_000 \
#         + result[2] * 31_104_000 \
#         + result[3] * 3600 \
#         + result[4] * 60 \
#         + result[5] 
    
#     # Calculate difference between timezones
#     mult1 = int(td_t1[0] + "1")
#     mult2 = int(td_t2[0] + "1")

#     result_td = (
#         (mult1 * int(td_t1[2]) - mult2 * int(td_t2[2])) * 3600
#         + (mult1 * int(td_t1[3]) - mult2 * int(td_t2[3])) * 60
#         + (mult1 * int(td_t1[4]) - mult2 * int(td_t2[4]))
#     )
    
#     return (str(abs(diff_time - result_td)))