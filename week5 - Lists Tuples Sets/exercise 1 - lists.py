"""
Write a program which uses a loop to input the hits per day of the top 10 Linux distributions and
append them to a list. After the values have been added to the list, the program should sort the list
in reverse order and display it, and then calculate and display the total, average, median, maximum
and minimum hits per day
"""

distros_list = []


number_of_values = int(input("input the number of distros \n"))

# Get all the values in the list from input
for i in range(number_of_values):
    hits_per_day = int(input("input the hits per day \n"))
    distros_list.append(hits_per_day)

distros_list.sort()
length = len(distros_list)

for i in distros_list:
    print(i)

print(f"Total hits per day : {sum(distros_list)}")
print(f"Average hits per day : {distros_list}")

# Get the list median value
if length % 2 != 0 :
    length_half = length/2
    middle_value = float(len(distros_list))/2
    print(f"Median hits per day : {middle_value}")
else :
    length = length + 1
    length_half = length / 2
    combined_middle = distros_list[int(length_half)] + distros_list[int(length_half - 1)]

    average_middle = combined_middle / 2
    print(f"Median hits per day : {average_middle}")

print(f"Min hits per day : {min(distros_list)}")
print(f"Max hits per day : {max(distros_list)}")