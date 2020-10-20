# Simple if elif else statement

number_of_dependants = 456

if number_of_dependants < 4 and number_of_dependants >= 0:
    print("Income limit is : 39875")
elif number_of_dependants >= 4 and number_of_dependants <= 7:
    print("Income limit is : 43810")
elif number_of_dependants >= 8:
    print("Income limit is : 47575")
else:
    print("Invalid input")



# Simple if elif else statement

import math

choice = int(input("Program for power ratio conversions \n1. Power to dBm \n2. dBm to Power \n"))

if choice == 1:
    power = float(input("Enter power in Mililwatts \n"))
    dBm = 10 * math.log10(power)
    print(f"dBm  is {dBm}")
elif choice == 2:
    dBm = float(input("Enter dBm in decibles \n"))
    power = 10 ** (dBm/10)
    print(f"power ratio is {round(power , 1)}")
else:
      print("invalid input")

     

# Simple if elif else statement
     
email = input("Enter email address \n")

if email[0:3] == "A00" and email.endswith("@student.ait.ie"):
    print("Valid Student Email")
elif email.endswith("@ait.ie"): 
    print("Valid staff Email")
else :
     print("invalid Email")