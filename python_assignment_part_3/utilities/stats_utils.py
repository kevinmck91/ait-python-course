import math

def get_mean(input_list: list) -> float:
    """
        Function Takes in a list of numbers and returns the average from the list

        Parameters
        ----------
            input_list - A list of integers or floats

        Returns
        -------
        TYPE
            float - The average value from the list

    """

    if (len(input_list)) > 0:
        return sum(input_list) / len(input_list)
    else:
        return "null"
    return

def get_median(input_list: list) -> float:

    """
        Function Takes in a list of numbers and returns the median value from the list

        Parameters
        ----------
            input_list - A list of integers or floats

        Returns
        -------
        TYPE
            float - The median value from the list

    """

    input_list = sorted(input_list)
    length = len(input_list)

    if len(input_list) == 1:
        return input_list[0]
    elif len(input_list) == 0:
        return "null"

    if length % 2 != 0:
        length_half = length / 2
        middle_value = float(len(input_list)) / 2
        return middle_value
    else:
        length = length + 1
        length_half = length / 2
        combined_middle = input_list[int(length_half)] + input_list[int(length_half - 1)]
        average_middle = combined_middle / 2
        return average_middle

def get_mode(input_list: list) -> float:

    """
        Function Takes in a list of numbers and returns the most common value from the list

        Parameters
        ----------
            input_list - A list of integers or floats

        Returns
        -------
        TYPE
            float - The  most common value from the list

    """

    dictionary = {}

    if len(input_list) == 1:
        return input_list[0]
    elif len(input_list) == 0:
        return "null"

    for number in input_list:

        if number not in dictionary:
            dictionary[number] = 1
        else:
            dictionary[number] += 1

    return max(dictionary, key=dictionary.get)

def get_standard_deviation(input_list: list) -> float:

    """
        Function Takes in a list of numbers and returns computes standard deviation of the list

        Parameters
        ----------
            input_list - A list of integers or floats

        Returns
        -------
        TYPE
            float - The  most standard deviation of the list

    """
    if len(input_list) == 1:
        return input_list[0]
    elif len(input_list) == 0:
        return "null"

    deviations = [(x - get_mean(input_list)) ** 2 for x in input_list]
    standard_deviation = math.sqrt(sum(deviations)/len(input_list) - 1)
    return standard_deviation

def get_correlation(input_list1: list, input_list2: list) -> float:

    """
        Function Takes in two lists of numbers and returns the correlation between the lists

        Parameters
        ----------
            input_list - A list of integers or floats

        Returns
        -------
        TYPE
            float - The correlation between the lists

    """

    average_x = get_mean(input_list1)
    average_y = get_mean(input_list2)

    deviations_for_x = [x - average_x for x in input_list1]
    deviations_for_y = [y - average_y for y in input_list2]

    # For multiplying corresponding values in the two lists
    deviations_for_xy = [x * y for (x, y) in zip(deviations_for_x, deviations_for_y)]

    deviations_for_x_squ = [(x - average_x) ** 2 for x in input_list1]
    deviations_for_y_squ = [(y - average_y) ** 2 for y in input_list2]

    correlation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ)) * (sum(deviations_for_y_squ)))

    return correlation
