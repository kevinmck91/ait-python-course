import math

try :
    
    with open("./data/fifa1.csv" , encoding="utf8") as fifa_file :
        
        line_count = 1
        
        value_list = []
        wage_list = []
        
        for line in fifa_file:
            
            try : 
            
                if line_count == 1:
                    line_count = line_count + 1
                    continue
                
                idn , name, value, wage = line.split(",")
                
                value = value.strip("€").strip("M").strip("K")
                wage = wage.strip().strip("€").strip("M").strip("K")
                
                value_list.append(float(value))
                wage_list.append(float(wage))
                
            except :
                
                print(f"Was unable line {line}")
          
            
            line_count = line_count + 1
            
except :
    
     print("unable to locate file")
     
     
print(line_count)

average_value = sum(value_list) / len(value_list)
average_wage = sum(wage_list) / len(wage_list)

list_of_xy = [(x - average_value) * (y - average_wage) for (x,y) in zip(value_list, wage_list)]
top_line = sum(list_of_xy)

list_of_x = [(x - average_value) ** 2 for x in value_list]
list_of_y = [(y - average_wage) ** 2 for y in wage_list]

bottom_line = math.sqrt(sum(list_of_x) * sum(list_of_y))

print("r : " , top_line / bottom_line)
     