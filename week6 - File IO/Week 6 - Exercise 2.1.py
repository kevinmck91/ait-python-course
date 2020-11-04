
sw_names_list = []

with open("data/names2.txt") as names_file:
    
    for my_line in names_file:
        
        split_string = my_line.split(" ")
        
        first_name = split_string[0]
        second_name = split_string[1]
        maiden_name = split_string[2]
        birth_place = split_string[3]
        
        sw_name = first_name[:3].capitalize() + second_name[:2] + " " + maiden_name[:2].capitalize() + birth_place[:3]
       
        sw_names_list.append(sw_name)
        
        print(f"sw_name : {sw_name}")
        

with open("data/generated_StarWars_names.txt" , "w") as out_file:
    
    for x in sw_names_list:
            out_file.write(x + "\n")