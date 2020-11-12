"""

Write a Python function which
– takes 3 parameters representing the total disk space, the amount used and the minimum
acceptable percentage free space
– calculates and displays the percentage of free space.
– and displays a message indicating whether or not there is sufficient disk space (at least the
minimum available)

"""

def is_there_free_space(total_space, used_space, minimum_acceptable_freespace) :

    free_space_precentage = (total_space - used_space) / total_space * 100

    print(f"Free space : {free_space_precentage} %")

    if free_space_precentage < 5:
        print(f"Warning ! low space")

    if free_space_precentage >= minimum_acceptable_freespace :
        return "Not enough space"
    else :
        return "enough space available"

result = is_there_free_space(500, 490, 35)

print(result)