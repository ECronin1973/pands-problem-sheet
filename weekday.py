# weekday.py
# this program will print whether the day the program is run
# is a weekday or a weekend, with a related comment
# Author: Edward Cronin

import datetime  #Import datetime module

from datetime import datetime 
# Python datetime module provides various functions to 
# create and manipulate the date and time

dt = datetime.now()  #Create datetime object
# The datetime module has a datetime class that contains 
# the current local date and time

today = dt.isoweekday()
# isoweekday() method is used to get the day of the week as an integer, 
# where Monday is 1 and Sunday is 7.

if today < 5: # 0 - 4 weekdays
    print(f"Yes, unfortunately today is a weekday")
# if command is used to give message where today is < 5 in day number where it falls during 
# the week, where monday starts as a zero and Friday is four

else:  # 5 sat, 6 sun 
    print(f"It is the weekend, yay!")
# else command will print message where today is 5th or 6th day number of the week 

# source: https://pynative.com/python-get-the-day-of-week/