"""
Write a function which takes as parameter a list of numbers and returns the median value in the list,
or None if the list is empty or not a list of numbers. (Use an if statement and the function from
Exercise 13).

"""

def get_median_value(values) :

    if(len(values)) > 0 :

        values.sort()

        if len(values) % 2 == 0 :
            length = len(values)
            return values
        else :
            length = len(values)
            index  = ((length + 1) / 2) - 1
            return values[int(index)]
    else :
        return "-1"


    print(values)

values = [1,2,3,4,5,6,7]
print(get_median_value(values))