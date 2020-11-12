"""

Create an empty dictionary (e.g. called frequencies)
For each number in the list
If the number is not already in the dictionary
Insert the number in the dictionary as the key, with a value of 1
Else
Increase by 1 the value of the dictionary item corresponding to the number
Return the key associated with the maximum value

"""

def calc_mode2(numbers):

    frequency_dict = {}

    for number in list:

        if number not in frequency_dict:
            frequency_dict[number] = 1
        else:
            frequency_dict[number] += 1

    print(frequency_dict)

    # Return the key associated with the maximum value
    print ("calc_mode2 : " , f"{max(frequency_dict, key=frequency_dict.get)} appears {max(frequency_dict.values())} times" )



def calc_mode3(numbers):

    # Create a dictionary with the frequencies
    frequencies = {number: numbers.count(number) for number in numbers}

    print(frequencies)

    # Return the key associated with the maximum value
    print ("calc_mode3 : " , max(frequencies, key=frequencies.get))



## Applicaion
from random import randint

list = [randint(1, 10) for x in range(1, 100)]

calc_mode2(list)
calc_mode3(list)