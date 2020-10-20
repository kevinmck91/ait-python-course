### This program converts miles to kilometers
#miles = float(input("please enter the distance in miles : ").strip(" "))
miles = 3.1
kilometers = miles * 1.60934
kilometers = round(kilometers,2)                # How to round / format a decimal
print(f"{miles} is : {kilometers} Kilometes \n")


### This program calculates download speeds
filesize = 10.0
speed = 1.544
downloadTime = (filesize*8.388608)/speed
downloadTime = "{:.2f}".format(downloadTime)    # How to format a decimal
print(f"A file size of {filesize} Mbs, with a speed of {speed} Mbps, will download in : {downloadTime} seconds \n")


### This program calculates area and perimeter
length = 3
width = 8
print(f"Area of rectangle is {length * width}. Perimeter of rectangle is {2*(length + width)} \n" )


### This program converts feet and inches to meters
feet = 29
inches = 2.5
totalInches = (12*feet)+inches
centimeters =  totalInches * 2.54
meters = centimeters/100
print(f'{feet}"{inches} is equal to {round(meters,4)} meters \n')


# Test out the methods that can be used with strings
sentence = "The quick black fox jumped over the lazy sleeping dog"
print("Sentence Length : ", len(sentence))
print("First Character : ", sentence[0])    #Strings are immutible
print("First Character : ", sentence[len(sentence) - 1])
print("UpperCase : ", sentence.capitalize())
print("LowerCase : ", sentence.lower())
print("Titled : ", sentence.title())
print("SwapCase : ",  sentence.swapcase())
print("Number of Spaces : ",  sentence.count(" "), "\n")


# Create username from a Fullname
fullname = "Kevin Mckeon"
print(f"{fullname=}")   #Output a vairable and its content
firstname , lastname = fullname.split()
username = firstname[0:3] + lastname[0:3]
username = username.lower()
print(f"Your usernae is : {username}")


# Print out the help DOC of a thing
import math;
help(math)


# Random roll a dice
from random import randint
rollOne = randint(1,6)
rollTwo = randint(1,6)
print("Rolling two dice : " , rollOne + rollTwo, "\n")


# Get a random charactor from a string
import string
from random import choice
print(string.ascii_letters + "\n")
choice(string.ascii_letters)


# Generate a Random Password
randomOne = randint(1,100)
wordOne = "apple"
wordTwo = "speakers"
print(f"Generated password : {wordTwo + choice(string.ascii_letters) + wordOne + choice(string.punctuation)}", "\n")


# Math Square Root - is a float
power = 27
resistance = 3
voltage = math.sqrt(power*resistance)
print(f"{voltage=}" , "\n")


# Square root and round function
mms = 1460
rtt = 0.03729
ploss = 0.001
limit = mms/(rtt * math.sqrt(ploss))
print(f"Limit is : {round(limit, 2)}" , "\n")


# Square root and round function
inductance = 1.5
capacitance = 0.000000039
frequnecy = 1/(2*math.pi*math.sqrt((inductance*capacitance)))
print("Frequency = ", round(frequnecy, 3), "\n")


# Math.hypot function
x1 = -2
y1 = 1
x2 = 1
y2 = 5
print("Distance between points ", math.hypot(x1-x2, y1-y2), "\n")


# Roots of quadratic Equation
a = 2
b = -5
c = -3
determinant =  b**2 - 4*a*c
root1 = (-1*b + math.sqrt(determinant))/(2 * a)
root2 = (-1*b - math.sqrt(determinant))/(2 * a)
print("The two roots are : " , root1, root2)


# surface area of a ball
a = 15
b = 10
e = math.sqrt(a**2 - b**2) / a
s = 2*math.pi*b*(b + (a*math.asin(e))/(e))
print(f"Surface Area of the ball is : {s:2f}" )


# velocity of a wave
gravity = 9.81
wavelength = 0.5
density = 1
sTension = 1.1
depth = 2

velocity = math.sqrt(
    (((gravity*wavelength)/(2*math.pi)) + ((2*math.pi*sTension)/(density*wavelength)))*(math.tanh((2*math.pi*depth)/wavelength))
)
print("Velocity = ", round(velocity, 2))