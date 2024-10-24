# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:19:54 2024

@author: DELL
"""

month= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 
        10: 31, 11: 30, 12: 31}
num= int(input("Enter the month number: "))
if (num>=1 and num<=12):
    print(f"The number of days in month {num} is {month[num]}")
else:
    print("Invalid. Please enter a number between 1 and 12.")
    
"""
Advanced Requirement:
"""
    
def year(leap_year):  #checking the leap year.
    return(leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0)
month= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 
            10: 31, 11: 30, 12: 31}
num= int(input("Enter the month number: "))
if num==2:
   leap_year=int(input("Enter the year: ")) 
   if year(leap_year):
       print("February in a leap year has 29 days.") 
   else:
        print("February has 28 days.")  
elif (num>=1 and num<=12):              
    print(f"The number of days in month {num} is {month[num]}")
else:
    print("Invalid. Please enter a number between 1 and 12.")