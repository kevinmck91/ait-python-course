"""
Read in a file and get the values
"""

with open("./data/supercomputers.txt") as super_computers_file:
    
    full_list = [float(x.strip()) for x in super_computers_file]

    print(f"Number of values : {len(full_list)} ") 
    print(f"Average Number : {sum(full_list) / len(full_list)}") 
    print(f"Maximum number : {max(full_list)} ") 
    print(f"Minimum number :  {min(full_list)}")
    
    full_list.sort()
    
    if len(full_list) % 2 != 0:
        median = full_list[int(((len(full_list) + 1) / 2 ) - 1)]
        print(f"Median number :  {median}") 
    else:
        value_1 = full_list[int(len(full_list)/2 - 1)] 
        value_2 = full_list[int(len(full_list)/2 - 1)]
        median = (value_1 + value_2) / 2
        print(f"Median number :  {median}") 
        
    
        import math
        
        list_of_sums = [(x - sum(full_list) / len(full_list))**2 for x in full_list]
       
        standard_dev = math.sqrt(sum(list_of_sums)/len(full_list))
        
        print(f"Standard dev :  {standard_dev}") 
    