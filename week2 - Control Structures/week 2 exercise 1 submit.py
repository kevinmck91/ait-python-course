# Program to generate a Star Wars name by A00279670

firstname = input("Enter firstname : ").strip(" ")
lastname = input("Enter lastname : ").strip(" ")
maiden_name = input("Enter Maiden Name : ").strip(" ")
birth_place = input("Enter Birth place : ").strip(" ")


# [0:3] include index 0 but exclude index 3
# [2:4] would include index 2 but not include index 4

sw_firstname = firstname[0:3].capitalize() + lastname[0:2].lower()
sw_lastname = maiden_name[0:2].capitalize() + birth_place[0:3].lower()


print(f"Your starwars name is : {sw_firstname} {sw_lastname} ")
