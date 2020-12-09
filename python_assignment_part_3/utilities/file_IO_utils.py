# A00279670

def parse_file(file_path: str, list_return_type: str) -> list:
    """
        This function is designed take in a File Path and a Return type.

        Parameters
        ----------
        file_path : The path of the file that is to be parsed
        list_return_type : The variable/Column that is required as an output. Possible parameters include
            - date
            - average_price
            - total_volume
            - 4046
            - 4225
            - 4770
            - total_bags
            - small_bags
            - large_bags
            - xlarge_bags
            - type
            - year
            - list_region
        Returns
        -------
        TYPE
            List - a list of the required type is returned

        """

    ### Import the file with try/except and split each line into a seperate set of strings
    ### store each string of the same type to a list for processing
    try:

        with open(file_path, encoding="utf8") as input_file:

            line_count = 1

            # Create a set of empty lists
            list_id = []
            list_date = []
            list_average_price = []
            list_total_volume = []
            list_4046 = []
            list_4225 = []
            list_4770 = []
            list_total_bags = []
            list_small_bags = []
            list_large_bags = []
            list_xlarge_bags = []
            list_type = []
            list_year = []
            list_region = []

            # For each line in the file...
            for line in input_file:

                try:

                    if line_count == 1:
                        line_count = line_count + 1
                        continue

                    value_id, value_date, value_average_price, value_total_volume, value_4046, value_4225, value_4770, value_total_bags, value_small_bags, value_large_bags, value_xlarge_bags, value_type, value_year, value_region = line.split(
                        ",")

                    # Return a column from the list depending on User Input
                    if list_return_type == "id":
                        value_id = value_id.strip()
                        list_id.append(float(value_id))
                    if list_return_type == "date":
                        value_date = value_date.strip()
                        list_date.append(value_date)
                    if list_return_type == "average_price":
                        value_average_price = value_average_price.strip()
                        list_average_price.append(float(value_average_price))
                    if list_return_type == "total_volume":
                        value_total_volume = value_total_volume.strip()
                        list_total_volume.append(float(value_total_volume))
                    if list_return_type == "4046":
                        value_4046 = value_4046.strip()
                        list_4046.append(float(value_4046))
                    if list_return_type == "4225":
                        value_4225 = value_4225.strip()
                        list_4225.append(float(value_4225))
                    if list_return_type == "4770":
                        value_4770 = value_4770.strip()
                        list_4770.append(float(value_4770))
                    if list_return_type == "total_bags":
                        value_total_bags = value_total_bags.strip()
                        list_total_bags.append(float(value_total_bags))
                    if list_return_type == "small_bags":
                        value_small_bags = value_small_bags.strip()
                        list_small_bags.append(float(value_small_bags))
                    if list_return_type == "large_bags":
                        value_large_bags = value_large_bags.strip()
                        list_large_bags.append(float(value_large_bags))
                    if list_return_type == "xlarge_bags":
                        value_xlarge_bags = value_xlarge_bags.strip()
                        list_xlarge_bags.append(float(value_xlarge_bags))
                    if list_return_type == "type":
                        value_type = value_type.strip()
                        list_type.append(value_type)
                    if list_return_type == "year":
                        value_year = value_year.strip()
                        list_year.append(float(value_year))
                    if list_return_type == "list_region":
                        value_region = value_region.strip()
                        list_region.append(value_region)

                except Exception as e:

                    # Write any parse exceptions to the log and print a note of the error to the user
                    with open("./log.txt", "a") as log_file:
                        log_file.write(f"Unable line parse line : {line_count} of the file {file_path} : {e} \n")
                        log_file.close()
                    print(f"Note : Unable to parse line : {line_count} of the file {file_path}\n")

                line_count = line_count + 1

        # If no file_path exception has occurred write to the log that the
        with open("./log.txt", "a") as log_file:
            log_file.write(f"The word file has been opened and parsed successfully \n")
            log_file.close()

    except Exception as e:

        with open("./log.txt", "a") as log_file:
            log_file.write(f"Unable to locate the file {file_path} : {e} \n")
            log_file.close()
        print(f"Unable to locate file {file_path}")
        return -1

    if list_return_type == "id":                  return list_id
    elif list_return_type == "date":              return list_date
    elif list_return_type == "average_price":     return list_average_price
    elif list_return_type == "total_volume":      return list_total_volume
    elif list_return_type == "4046":              return list_4046
    elif list_return_type == "4225":              return list_4225
    elif list_return_type == "4770":              return list_4770
    elif list_return_type == "total_bags":        return list_total_bags
    elif list_return_type == "small_bags":        return list_small_bags
    elif list_return_type == "large_bags":        return list_large_bags
    elif list_return_type == "xlarge_bags":       return list_xlarge_bags
    elif list_return_type == "type":              return list_type
    elif list_return_type == "year":              return list_year
    elif list_return_type == "list_region":       return list_region
    else:                                        return "None"

