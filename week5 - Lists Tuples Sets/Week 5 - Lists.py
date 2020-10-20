hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
values = [4,5,6,7,5,4,3,2]
nonsense = [1, 2, 'buckle my shoe', 3, 4, 'knock on the door']
strings = ["abc", "123", "kevin", "tom", "alan"]
# all_numbers = list(range(1,48)) # a list of values from 1 to 10
#my_numbers = list()     # Creates an empty list





print(len(values))          # Prints the lenght
print(sum(values))          # Prints the sum of the values
print(sorted(values))       # The sorted() function will create a new list containing a sorted version of the list it is given
print(values.sort())        # sort() function will modify the list it is called on.
print(min(values))          # Prints the minimum valus of the list - must be all the same type
print(max(strings))         # Prints the max valus of the sorted list - must be all the same type
print("")


# Both valid ways to check if a value is in a list (or not)
if "abc" not in strings:
    pass
if not "abc" not in strings:
    pass



# Apending a value to the list
strings.append("appended value")
print(strings)
print("")



numbers = [1,2,3,4,5,6,7,8,9]

# Choose a random value off a list
from random import choice
random_number = choice(numbers)
print("random_number =", random_number)


# Shuffle the list of numbers
from random import shuffle
shuffle(numbers)
print("numbers =", numbers)


# get first 6 numbers off the list (index 0 to 5)
print("numbers =", numbers[:6])


# Create an empty list of size 26
frequencies = [0] * 26
print("frequencies =", frequencies)

# List operations
values.insert(4,7)      # insert x at position i
values.remove(6)        # Remove first item equal to 6
values.pop(3)           # Remove the item at the given position i in the list, and return it If no index is specified, pop() removes and returns the last item in the list
values.count(4)         # Count the number of times a value appears
print(values)
values.sort()
print(values)
values.reverse()
print(values)
print("")



# Lists and loops - Printing out a list
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
for day in weekdays:
    print(day)

print('wed' in weekdays)        # Returns a boolean
print("")



# you can print cerain elements of a list all in the one line 
# :< and :> format the output by moving and inserting whitespace
for word in weekdays:
    print(f"{word:<8} {len(word):>4}")
print("")


# getting an element from a list
print(weekdays[3])      # Must pass in an its
print(weekdays[3:5])    # gets a subset of a list
print("")




# Splitting a string creates a list
myString = "Splitting a string creats a list"
myList = myString.split(" ")
print(myList)
print("")




# Joining a string creates a list
newString = " ".join(myList)
print(newString)
print("")





# Joining two lists together
users = ["kevin" , "paul" , "eoin"]
new_users = ["eamon", "Enda", "richie"]
all_users = users + new_users
print(all_users)
print("")





# List comprehension is a shorthand way of creating a list
squares = [x**2 for x in range(11)]     ## add x to the power of two for each element between 0 and 11
print(squares)
print("")




# In general, a list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses:

squares = [x**2 for x in range(11) if x % 2 == 0]
print(squares)
print("")




sentence = "Hello my name is kevin and I am writing python"
# Get a list of each length for each word
lenghts = [len(word) for word in sentence.split()]  
print("lenghts = " , lenghts)
print("")




# For multiplying corrosponding values in two lists use the Zip
list_of_x = [5,7,9,3,5,1]
list_of_y = [2,4,6,8,1,6]
list_of_xy = [x*y for (x,y) in zip(list_of_x, list_of_y)]
print("list_of_xy = " , list_of_xy)
print("")