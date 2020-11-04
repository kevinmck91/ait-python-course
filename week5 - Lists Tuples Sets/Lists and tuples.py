print("\n\n 1. Types of lists ******************************************************************************************** \n\n")    


hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
values = [4,5,6,7,5,4,3,2]
nonsense = [1, 2, 'buckle my shoe', 3, 4, 'knock on the door']
strings = ["abc", "123", "kevin", "tom", "alan"]
# all_numbers = list(range(1,48)) # a list of values from 1 to 10
#my_numbers = list()     # Creates an empty list




print("\n\n 2. Lists methods ******************************************************************************************** \n\n")    

print(len(values))          # Prints the lenght
print(sum(values))          # Prints the sum of the values
print(sorted(values))       # The sorted() function will create a new list containing a sorted version of the list it is given
print(values.sort())        # sort() function will modify the list it is called on.
print(min(values))          # Prints the minimum valus of the list - must be all the same type
print(max(strings))         # Prints the max valus of the sorted list - must be all the same type




print("\n\n 3. Check if a list has a value ******************************************************************************************** \n\n")    

# Both valid ways to check if a value is in a list (or not)
if "abc" not in strings:
    pass
if not "abc" not in strings:
    pass





print("\n\n 4. Apending a value to the list ******************************************************************************************** \n\n")    

strings.append("appended value")
print(strings)





print("\n\n 5. Choose a random value off a list ******************************************************************************************** \n\n")    

numbers = [1,2,3,4,5,6,7,8,9]

from random import choice
random_number = choice(numbers)
print("random_number =", random_number)




print("\n\n 6. Shuffle the list of numbers ******************************************************************************************** \n\n")    

from random import shuffle
shuffle(numbers)
print("numbers =", numbers)




print("\n\n 7. get first 6 numbers off the list ******************************************************************************************** \n\n")    

# get first 6 numbers off the list (index 0 to 5)
print("numbers =", numbers[:6])




print("\n\n 8. Create an empty list ******************************************************************************************** \n\n")    

# Create an empty list of size 26
frequencies = [0] * 26
print("frequencies =", frequencies)




print("\n\n 9. List operations ******************************************************************************************** \n\n")    

# List operations
values = [4,5,6,7,5,4,3,2]


values.insert(4,7)      # insert x at position i
values.remove(6)        # Remove first item equal to 6
values.pop(3)           # Remove the item at the given position i in the list, and return it If no index is specified, pop() removes and returns the last item in the list
values.count(4)         # Count the number of times a value appears
print(values)
values.sort()
print(values)
values.reverse()
print(values)



print("\n\n 10. Lists and loops ******************************************************************************************** \n\n")    


# Lists and loops - Printing out a list
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
for day in weekdays:
    print(day)

print('wed' in weekdays)        # Returns a boolean





print("\n\n 11. Printing out a list ******************************************************************************************** \n\n")    

# you can print cerain elements of a list all in the one line 
# :< and :> format the output by moving and inserting whitespace
for word in weekdays:
    print(f"{word:<8} {len(word):>4}")




print("\n\n 12. getting an element from a list ******************************************************************************************** \n\n")    

print(weekdays[3])      # Must pass in an its
print(weekdays[3:5])    # gets a subset of a list





print("\n\n 13. Spliiting string ******************************************************************************************** \n\n")    

# Splitting a string creates a list or an individual variables
myString = "Splitting a string creats a list"
myList = myString.split(" ")
print(myList)





print("\n\n 14. Joining a string creates a list ******************************************************************************************** \n\n")    

newString = " ".join(myList)
print(newString)




print("\n\n 15. Joining two lists together ******************************************************************************************** \n\n")    

users = ["kevin" , "paul" , "eoin"]
new_users = ["eamon", "Enda", "richie"]
all_users = users + new_users
print(all_users)




print("\n\n 16. List comprehension ******************************************************************************************** \n\n")    

# List comprehension is a shorthand way of creating a list
squares = [x**2 for x in range(11)]     ## add x to the power of two for each element between 0 and 11
print(squares)



print("\n\n 17. List comprehension ******************************************************************************************** \n\n")    

# In general, a list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses:
squares = [x**2 for x in range(11) if x % 2 == 0]
print(squares)



print("\n\n 18. Getting a list of word lenghts ******************************************************************************************** \n\n")    

sentence = "Hello my name is kevin and I am writing python"
lenghts = [len(word) for word in sentence.split()]  
print("lenghts = " , lenghts)




print("\n\n 19. use the Zip ******************************************************************************************** \n\n")    


# For multiplying corrosponding values in two lists use the Zip
list_of_x = [5,7,9,3,5,1]
list_of_y = [2,4,6,8,1,6]
list_of_xy = [x*y for (x,y) in zip(list_of_x, list_of_y)]
print("list_of_xy = " , list_of_xy)
print("")