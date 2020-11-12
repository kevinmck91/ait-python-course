print("\n 1. Epoch Time ************************************************************************\n")

import time

print("number of seconds since the Unix Epoch" , time.time())
print("")
print("Return a complete date/time structure based on a given Epoch time : \n" , time.gmtime(1205106445.353038))
print("")
print("Return the current date/time structure based on a given Epoch time : \n" , time.gmtime())
print("")
print("Current local time : \n " , time.localtime())



print("\n 2. The Date/Time module for dates only ************************************************************************\n")

# The datetime Module provides the a number of classes for working with date/time
# date - year, month, and day.
# time - hour, minute,  second, microsecond, and tzinfo (timezone information).
# datetime - year, month, day, hour, minute, second, microsecond, and tzinfo.
# timedelta - A duration expressing the difference between two date, time, or datetime

import datetime

# Takes in a date (in ISO format)
new_years_eve = datetime.date(2020,12, 31)
print("new_years_eve", new_years_eve)
print(new_years_eve.year)
print(new_years_eve.month)
print(new_years_eve.day)

print("")

# Takes in todays date
today = datetime.date.today()
print("today", today)
print(today.year)
print(today.month)
print(today.day)

print("")

# Takes in a date in ISO format
fools_day = datetime.date.fromisoformat("2020-04-01")
print("fools_day", fools_day)
print(fools_day.year)
print(fools_day.month)
print(fools_day.day)

print("")

# prints a date in ISO format
print(new_years_eve.isoformat())




print("\n 3.  The Date/Time module for time only ************************************************************************\n")

#  datetime.datetime
# create a timedelta object by specifying the number of days, seconds, microseconds, # milliseconds, minutes, hours, and or weeks


my_time = datetime.time(16, 59, 59)
print(my_time)

my_time2 = datetime.time(16, 59, 59)
print(my_time)



print("\n 4  The Date/Time module for both date & time ************************************************************************\n")

new_years_eve_date_and_time = datetime.datetime(2020,12, 31, 12, 59,59)
print(new_years_eve_date_and_time)



print("\n 5. Date/Time Formatting using datetime ************************************************************************\n")

my_date = datetime.date(2020,11,3)
print(my_date.strftime("%d/%m/%y"))
print(my_date.strftime("%A / %d / %B / %Y"))

my_date = my_date.replace(year=2000, month=4, day=5)

print(my_date.strftime("%d %m %y -- %A / %d / %B / %Y"))



print("\n 6.  Date/Time module with  time Delta ************************************************************************\n")

early_date = datetime.date.fromisoformat("2018-09-21")
latest_date = datetime.date.fromisoformat("2020-04-01")

print("")

delta = latest_date - early_date
print("Number of days between early_date and latest_date ", delta.days)
