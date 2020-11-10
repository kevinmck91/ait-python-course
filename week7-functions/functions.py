print("\n 1. Function Definition ************************************************************************\n")
        
from import_functions import hello
hello()

def my_function1():
    print("this code block is in a function")
    

my_function1()

    
    

print("\n 2. Function Parameters ************************************************************************\n")


   
def my_function2(name, location):
    print(f"Parameters Parameters passed in : {name} {location}")
    
my_function2("kevin", "mullingar")
 



print("\n 3. Inclusive functions ************************************************************************\n")

help(round)

my_float = 3.23466
print(round(my_float, 3))

print(round(22/7, 10))



print("\n 3. Default Parameters ************************************************************************\n")

from random import randint

def roll_dice(num_dice=2):          # You cannot have a non-default parameter after a default parameter. 
    
    total = 0
    print(f"You rolled : {num_dice} dice")
     
    for i in range(num_dice):
        number = randint(1,6)
        total += randint(1,6)
        
    print("total : " , total)
    
roll_dice()
roll_dice(4)
        


print("\n 3. global variables ************************************************************************\n")

def get_a_word():
    global value
    value = "kevin"

try: 
    print(value) 
except:
    print("Value is not in scope")  
    
get_a_word()
print(value , "Value is in scope after running function (bad practice)")  
    
 
    
print("\n 3. Return Statement ************************************************************************\n")

def multiply(n , m):
    return n * m

result = multiply(4,7)

print(result)




print("\n 3. Return Multiple Elements ************************************************************************\n")

def get_result_and_remainder(dividend, divisor):
    return(round(dividend / divisor), dividend % divisor)
        

dividend = 102
divisor = 11


my_result , my_remainder = get_result_and_remainder(dividend, divisor)

print("result " , my_result)
print("remainder " , my_remainder)




print("\n 3. Doc String ************************************************************************\n")

def multiply_two_nums(n , m):
    """
    This function is designed to multiply two inputs and retun the result to the caller

    Parameters
    ----------
    n : Interger or Float
    
    m : Interger or Float

    Returns
    -------
    TYPE
        flaot.

    """
    return n * m

help(multiply_two_nums)



print("\n 3. pydoc ************************************************************************\n")


# run these in the command line
# pydoc multiply_two_nums


print("\n 3. Function Annotations ************************************************************************\n")

def greeting(name: str) -> int :
    return len(name)

num_of_letters = greeting("KEVIN")
print("num_of_letters" , num_of_letters)

# When typing out the greeting function, it will popup with the input and output type
# function annotation is probably handier thatn perfect docstrings
# python will use the annotation when generating the doc string



