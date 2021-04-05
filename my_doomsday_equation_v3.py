import math
import numpy as np
import sys
#What day

month = int(input("Print month here: "))
day = int(input("Print day here: "))
year = int(input("Print year here: "))


if year > 1582 or (year == 1582 and month > 10) or (year == 1582 and month == 10 and day >= 15):
    
    while year >= 1900:
        year -= 400

    if year in range(1500, 1600):
        base_day = 3
    elif year in range(1600, 1700):
        base_day = 2
    elif year in range(1700, 1800):
        base_day = 0
    elif year in range(1800, 1900):
        base_day = 5
else:
    print('Sorry, this date came before our current calendar system. I don\'t have the energy to compute that.')
    sys.exit()


#DOOMSDAY ADVANCER

last_two = abs(year) % 100

division_by_12 = last_two // 12
the_remainder = last_two % 12
if the_remainder >= 4:
	division_by_4 = the_remainder // 4
else:
	division_by_4 = 0

#doomsday = (division_by_12 + the_remainder + division_by_4 + base_day) % 7

my_dict = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

#dd_of_year = my_dict[doomsday]


#IS THIS A LEAP YEAR

non_leap_years = np.array([3, 0, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12])
leap_years = np.array([4, 1, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12])

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           leap_year = True
       else:
           leap_year = False
   else:
       leap_year = True
else:
   leap_year = False
   
#FINDING ADDITIONAL DISTANCE OF GIVEN DATE FROM DOOMSDAY

if leap_year is True:
    doomsday_of_month = leap_years[month - 1]
    if doomsday_of_month > day:
        final_add = -(doomsday_of_month - day) % 7 
    elif doomsday_of_month < day:
        final_add = (day - doomsday_of_month) % 7
    else:
        final_add = 0
        
    final_answer = (final_add + division_by_12 + the_remainder + division_by_4 + base_day) % 7
    #print(doomsday_of_month, final_add)
    #print(division_by_12, the_remainder, division_by_4, base_day, final_add, my_dict[final_answer])
    print(my_dict[final_answer])

if leap_year is False:
    doomsday_of_month = non_leap_years[month - 1]
    if doomsday_of_month > day:
        final_add = -(doomsday_of_month - day) % 7 
    elif doomsday_of_month < day:
        final_add = (day - doomsday_of_month) % 7
    else:
        final_add = 0
        
    final_answer = (final_add + division_by_12 + the_remainder + division_by_4 + base_day) % 7
    #print(doomsday_of_month, final_add)
    #print(division_by_12, the_remainder, division_by_4, base_day, final_add, my_dict[final_answer])
    print(my_dict[final_answer])

