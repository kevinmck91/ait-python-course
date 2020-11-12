sw_names_list = []

try :
    
    with open("data/names2.txt") as names_file:
        
        line_counter = 1
        
        for my_line in names_file:
            
            try :
                
                first_name , second_name , maiden_name, birth_place = my_line.split()
                
                sw_name = first_name[:3].capitalize() + second_name[:2] + " " + maiden_name[:2].capitalize() + birth_place[:3]
               
                sw_names_list.append(sw_name)
                
                print(f"sw_name : {sw_name}")
                
                line_counter = line_counter + 1
            
            except : 
               
                print("\nUnable to read this line of the file line : ", line_counter)
                print("line : ", my_line)

except FileNotFoundError:
    
    print("Unable to find file")

        

with open("data/generated_StarWars_names.txt" , "w") as out_file:
    
    for x in sw_names_list:
            out_file.write(x + "\n")