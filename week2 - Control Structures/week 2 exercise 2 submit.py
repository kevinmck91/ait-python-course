# Program to calcualte the time period of a pendulum by A00279670

import math

length = float(input("Enter the pendulum length in meters : "))
gravity = 9.81

time = (2 * math.pi * math.sqrt(length / gravity))

print(f"The time is : {round(time, 2)}" )