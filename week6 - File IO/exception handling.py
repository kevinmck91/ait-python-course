print("\n\n 1. ********************************************************************************************\n\n")    

try:
    
    with open("fake_file.txt") as fake_file:
        
        content = fake_file.read()
    
except:
    
    print("Unable to open the file")
    
print("Code continuing ..")
    


print("\n\n 2. ********************************************************************************************\n\n")    

try:
    
    with open("fake_file.txt") as fake_file:
        
        content = fake_file.read()
    
except FileNotFoundError:
    print("Unable to open the file")
except IsADirectoryError:
    print("file is a directory")
except PermissionError:
    print("Permission no allowed")
else : 
    print("No Exception arose, so print this code")
     
print("Code continuing ..")
    



print("\n\n 3. ********************************************************************************************\n\n")    

try:
    
    with open("fake_file.txt") as fake_file:
        
        content = fake_file.read()
    
except FileNotFoundError:
    print("Unable to open the file")
except IsADirectoryError:
    print("file is a directory")
except PermissionError:
    print("Permission no allowed")
else : 
    print("No Exception arose, so print this code")
finally :
    print("Finally will always print, regardless of exceptions")
    
print("Code continuing ..")