# Easy Level Problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

month, day, year = map(int, input().split(' '))

day_of_the_week = calendar.day_name[calendar.weekday(year, month, day)]

print(day_of_the_week.upper())