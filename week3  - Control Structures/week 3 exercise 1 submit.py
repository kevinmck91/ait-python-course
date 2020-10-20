# Program to validate a username by A00279670

username = input("Please enter your username : ")

# This method allows for more than one error message to flag at once
valid = True

if len(username) < 4 or len(username) > 8: 
    print("The username must be between 4 and 8 characters long")
    valid = False

if  not username[0].islower():
    print("The username must start with a lowercase letter")
    valid = False
     
if not username.isalpha():
    print("The username must be alpha numeric")   
    valid = False
    
if(valid):
     print("The username is valid") 
    
