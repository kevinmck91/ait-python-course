print("\n 1. Dictionary ************************************************************************\n")

# A Dictionary is a set of Key Value Pairs
# It can also be seen as a list with the keys instead of indexes
# The key cannot be a list. It has to be immutable
# Ordering is not preserved, Duplicated are not allowed

proxy = {
    'server' : 'proxy.ait.ie',
    'port' : 3128,
    'username' : 'a00123456'
}

empty_dict = {}

lang_1 = dict([ ("one" , "uno") , ("two" , "dos"), ("three" , "tres"), ("one" , "uno")])


print(proxy)

proxy["port"] = 8080

print(proxy.get('username'))
print(proxy.get(2, "test"))



print("\n 2. check if word is in Dictionary ************************************************************************\n")

# the 'in' operated tells you if a key is in the dictionary

if 'port' in proxy:
    print("port key is in proxy")

# To check if a dictionaly contains a values, convert the values to a

if 8080 in proxy.values():
    print("8080 value is in proxy")



print("\n 2. lists and tuples ************************************************************************\n")

list_of_keys = proxy.keys()
list_of_values = proxy.values()
list_of_tuples = proxy.items()

print(list_of_keys)
print(list_of_values)
print(list_of_tuples)



print("\n 2. Traversing a dictionary ************************************************************************\n")

# We can sort the keys and then travers the dictionary alphabetically
for word in sorted(lang_1):
    print(word, lang_1[word])



print("\n 2. Deleteing an element ************************************************************************\n")

del lang_1['two']
print(lang_1)



print("\n 2. Shelf module ************************************************************************\n")

# shelves are like Python dictionaries that are associated with an external file

import shelve

