# A00279670

def create_dictionary(list_1: list, list_2: list) -> dict:

    """
        This function is designed to take in two lists and return a dictionary of unique keys and accumulative values

        Parameters
        ----------
        list_1 - A categorical set of values
        list_2 - A set of figures where each figure corresponds to a category

        Returns
        -------
        dictionary {} - return a dictionary of unique keys and accumulative values

    """

    dict = {}

    for key, value in zip(list_1, list_2):

        if key in dict:
            current_value = dict[key]
            accumulative_value = current_value + value
            dict[key] = accumulative_value
        else:
            dict[key] = value

    return dict