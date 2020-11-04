import math

list_of_ages = []
list_of_ratings = []

with open("./data/fifa1.csv" , encoding="utf8") as fifa_file :
    
    array_of_lines = fifa_file.readlines()
    
    line_counter = 1
    
    for line in array_of_lines:
        
        try:
            
            player_id, name, age, rating = line.split(",")
        
            list_of_ages.append(int(age))
            list_of_ratings.append(int(rating))

        except:
            print("line in wrong format " , line)
  

average_age = sum(list_of_ages) / len(list_of_ages)
average_ratings = sum(list_of_ratings) / len(list_of_ratings)

list_of_xy = [(x - average_age) * (y - average_ratings) for (x,y) in zip(list_of_ages, list_of_ratings)]
top_line = sum(list_of_xy)

list_of_x = [(x - average_age) ** 2 for x in list_of_ages]
list_of_y = [(y - average_ratings) ** 2 for y in list_of_ratings]

bottom_line = math.sqrt(sum(list_of_x) * sum(list_of_y))

print("r : " , top_line / bottom_line)
    