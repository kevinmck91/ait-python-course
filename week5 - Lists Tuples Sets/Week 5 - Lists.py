hex_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
nonsense = [1, 2, 'buckle my shoe', 3, 4, 'knock on the door']
strings = ["abc", "123", "kevin", "tom", "alan"]
values =  list(range(10))  # a list of values from 1 to 10

print(len(values))          # Prints the lenght
print(sum(values))          # Prints the sum of the values
print(sorted(values))       # Sorts the values alphabetically or numerically - must be all the same type
print(min(values))          # Prints the minimum valus of the list - must be all the same type
print(max(strings))         # Prints the max valus of the sorted list - must be all the same type
print("")

# Addpending a value to the list
strings.append("appended value")
print(strings)
print("")

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