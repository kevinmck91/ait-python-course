print("\n\n 1. ********************************************************************************************\n\n")    


#  The default encoding is utf_8
#  Open a file and print every line (with two spaces. one for carrige and one for print())
#  Everyting is imported as a string

with open ("./data/test.txt") as my_text_file:
    
    for my_line in my_text_file:
        
        print(my_line)
        
        
        
        
print("\n\n 2. ********************************************************************************************\n\n")    


# .strip removes all the spaces, tabs and newlines from the start/end of a string
# The for loop statement stores each line of the file in the variable hero

with open ("./data/test.txt") as my_text_file:
    
    for my_line in my_text_file:
        
        my_line = my_line.strip()       #Strips out the \n character and reassignes
        print(my_line)
        
        
        
        
print("\n\n 3. ******************************************************************************************** \n\n")    

# Apparently python has a built in dictinonary ?

password = "facebook"

with open("./data/test.txt") as wordsfile:         
    
    for word in wordsfile : 
        
        if password == word.strip():
            
            print("Password cannot be a word")
            break
    
    else:
        print("Password is ok")
 
        
 
    
print("\n\n 4. ******************************************************************************************** \n\n")    

# Everythign is read in as a string and has to be converted into ints or floats

total = 0

with open("./data/numbers.txt") as numbers_file : 
    
    for number in numbers_file :
        
        current_number = int(number)            # cast a string to an int or float
        total += current_number
        
print(f"total is : {total}")




print("\n\n 5. ******************************************************************************************** \n\n")    

# Stats for a number file

with open("./data/numbers.txt") as numbers_file : 
    
     list_of_nums = [int(x.strip()) for x in numbers_file]
        
print(f"Number of values : {len(list_of_nums)} ") 
print(f"Total number : {sum(list_of_nums)} ") 
print(f"Average Number : {sum(list_of_nums) / len(list_of_nums)}") 
print(f"Maximum number : {max(list_of_nums)} ") 
print(f"Minimum number :  {min(list_of_nums)}") 




print("\n\n 6. ******************************************************************************************** \n\n")    


print(f"{'Name':20} Username")

with open("./data/my_names.txt") as names_file:
    
    for name in names_file : 
        
        name = name.strip()
        firstname, lastname = name.split()
        username = (firstname[0] + lastname).lower()
        print(f"{name:20} {username}")
        
        
        
print("\n\n 7. ******************************************************************************************** \n\n")    

# Check that a line is splitable first

print(f"{'Name':20} Username")

with open("./data/odd_names.txt") as names_file:
    
    for name in names_file : 
        
        name = name.strip()
        
        if name.count(" ") == 1:
            
            firstname, lastname = name.split()
            username = (firstname[0] + lastname).lower()
            print(f"{name:20} {username}")
        
            
            
print("\n\n 8. Lists and sublists ******************************************************************************************** \n\n")    

# Lists and sublists

with open("./data/avocado.csv") as dataset:

    row_num = 0   # to keep track of each line
    
    for line in dataset:
        
        line = line.strip()
        
        if row_num == 10 :
             break
        
        if row_num == 0 :
            
            headings = line.split(",")
            print(headings) 
            
        else :
            
            values = line.split(",", maxsplit=4)
            
            num = values[0]
            date = values[1]
            ave_prive = values[2]
            tot_vol = values[3]
            everything_else = [x for x in values[4].split(",") ]   # this is the sublist
            
            print(values)      
       
        row_num = row_num + 1
        
        
        
        
print("\n\n 9. .readLines()  ******************************************************************************************** \n\n")    

# .readlines returns a list with each list entry containing a line string

with open("./data/names.txt") as names_file:
    
    names_list = names_file.readlines()
    
    print(names_list)
 
# We can then loop over this list instead of reading the data from the file line by line
       
        
        
        
        
print("\n\n 10. .read() ******************************************************************************************** \n\n")    
     
# this method reads in the whole file as one string

with open("./data/names.txt") as names_file:
    
    names_list = names_file.read()      
    print(names_list) 

# We can then split every word into a dictionaly and do a word analysis     
        
        
        
 
        
print("\n\n 10. Read, Overwrite, Append ************************************************************************************** \n\n")    
  
# This method opend the file to read
with open("./data/names.txt") as names_file:   
    print("Read")
    
with open("./data/names.txt" , "r") as names_file:   
    print("Read with parameter")
    
with open("./data/names.txt", "w") as names_file:   
    print("Overwrite")
    
with open("./data/names.txt", "a") as names_file:   
    print("append")
    
    
# WRITING TO A FILE

with open("./data/lotto.txt", "w") as lotto_file:   
    
    lotto_file.write("Lotto numbers\n")
    lotto_file.write("5\n")                 # newline is required
    lotto_file.write(str(12) + "\n")        # can only write strings
    lotto_file.write("15\n")                # this will overwrite the file each time is run
  

# APPENDING TO A FILE

with open("./data/lotto.txt", "a") as lotto_file:   
     lotto_file.write("37\n")
     lotto_file.write("48\n")
     lotto_file.write("5\n")
                                                  
 