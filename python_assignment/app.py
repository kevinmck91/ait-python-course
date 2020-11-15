# A00679670

import math
file_path = "avocado.csv"

with open("./log.txt", "a") as log_file:
    log_file.write(f"\n***** The Application has been initialised ******  \n")
    log_file.close()

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

                value_id, value_date, value_average_price, value_total_volume, value_4046, value_4225, value_4770, value_total_bags, value_small_bags, value_large_bags, value_xlarge_bags, value_type, value_year, value_region = line.split(",")

                # Strip any unwanted whitespace
                value_id = value_id.strip()
                value_date = value_date.strip()
                value_average_price = value_average_price.strip()
                value_total_volume = value_total_volume.strip()
                value_4046 = value_4046.strip()
                value_4225 = value_4225.strip()
                value_4770 = value_4770.strip()
                value_total_bags = value_total_bags.strip()
                value_small_bags = value_small_bags.strip()
                value_large_bags = value_large_bags.strip()
                value_xlarge_bags = value_xlarge_bags.strip()
                value_type = value_type.strip()
                value_year = value_year.strip()
                value_region = value_region.strip()

                # Add each value to the list
                list_id.append(float(value_id))
                list_date.append(value_date)
                list_average_price.append(float(value_average_price))
                list_total_volume.append(float(value_total_volume))
                list_4046.append(float(value_4046))
                list_4225.append(float(value_4225))
                list_4770.append(float(value_4770))
                list_total_bags.append(float(value_total_bags))
                list_small_bags.append(float(value_small_bags))
                list_large_bags.append(float(value_large_bags))
                list_xlarge_bags.append(float(value_xlarge_bags))
                list_type.append(value_type)
                list_year.append(float(value_year))
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

    command = ""
    print(f"This application analysis the datafile {file_path} \n")

except Exception as e:

    with open("./log.txt", "a") as log_file:
        log_file.write(f"Unable to locate the file {file_path} : {e} \n")
        log_file.close()

    print(f"Unable to locate file {file_path}")

    command = "Q"


### This section analyzes the file depednig on user input on a Main Menu and Sub Menu Basis
while command != "Q":


### This section provides the user to choose an value off the Main menu
    command = input(
        "Please enter a command : \n"
        
        "1 - Basic Statistics : Get information and basic statistics about the data being analysed\n"
        "2 - Averages : Get the average for a specific data column \n"
        "3 - Standard Deviation : Get the Standard Deviation for a specific data column \n"
        "4 - Correlation: Get the Correlation between two data columns \n"
        "Q - Exit / Quit\n"
    ).upper()

    with open("./log.txt", "a") as log_file:
        log_file.write(f"The user has chosen option : '{command}' from the main menu \n")
        log_file.close()

    print(" ")

    if command == "Q":

        break

    ### if the user chooses 2 from the main menu...
    elif command == "2":

        ### Show the user the Sub-menu-1
        command_one = input(
            "   Get the average price of an avocado over the 4 year period\n"
            "   Please enter a number corresponding to the instruction : \n"
            "   1 - Average Price of an individual avocado over a 4 year period\n"
            "   2 - Average amount of a small bags of avocados sold per day over a 4 year period\n"
            "   3 - Average amount of a large bags of avocados sold per day over a 4 year period\n"
            "   4 - Average amount of a x-large bags of avocados sold per day over a 4 year period\n"
        )

        with open("./log.txt", "a") as log_file:
            log_file.write(f"The user has chosen sub-option : '{command_one}' from the sub-menu \n")
            log_file.close()

        ### Sub-menu-1 Option 1
        if command_one == "1":
            print(f"    Average Price of an individual avocado over a 4 year period : € {str(round(sum(list_average_price) / len(list_average_price), 2))}\n")

        ### Sub-menu-1 Option 2
        elif command_one == "2":
            print(f"    Average amount of a small bags of avocados sold per day over a 4 year period : {str(round(sum(list_small_bags) / len(list_small_bags), 2))} bags\n")
        ### Sub-menu-1 Option 3
        elif command_one == "3":
            print(f"    Average amount of a large bags of avocados sold per day over a 4 year period : {str(round(sum(list_large_bags) / len(list_large_bags), 2))} bags\n")

        ### Sub-menu-1 Option 4
        elif command_one == "4":
            print(f"    Average amount of a x-large bags of avocados sold per day over a 4 year period : {str(round(sum(list_xlarge_bags) / len(list_xlarge_bags), 2))} bags\n")

        ### Sub-menu-1 Option invlaid
        else:
            print(f"    {command_one} is an invalid selection\n")


    ### if the user chooses 3 from the main menu...
    elif command == "3":

        ### Show the user the Sub-menu-2
        command_two = input(
            "   Standard Deviation of an avocado over the past 4 years \n"
            "   Please enter a number corresponding to the instruction : \n"
            "   1 - Standard Deviation of an avocado price over a 4 year period\n"
            "   2 - Standard Deviation of the amount of small bags of avocados sold over a 4 year period\n"
            "   3 - Standard Deviation of the amount of large bag of avocados sold over a 4 year period\n"
            "   4 - Standard Deviation of the amount of X-large bag of avocados sold over a 4 year period\n"
        )

        with open("./log.txt", "a") as log_file:
            log_file.write(f"The user has chosen sub-option : '{command_two}' from the sub-menu \n")
            log_file.close()

        ### Sub-menu-2 Option 1
        if command_two == "1":
            average = sum(list_average_price) / len(list_average_price)
            value_minus_average = [(x - average) ** 2 for x in list_average_price]
            result = sum(list_average_price) / (len(list_average_price) - 1)
            standard_deviation = math.sqrt(result)
            print(f"    Standard Deviation of an individual avocado price over a 4 year period : {str(round(standard_deviation, 3))}\n")

        ### Sub-menu-2 Option 2
        elif command_two == "2":
            average = sum(list_small_bags) / len(list_small_bags)
            value_minus_average = [(x - average) ** 2 for x in list_small_bags]
            result = sum(list_small_bags) / (len(list_small_bags) - 1)
            standard_deviation = math.sqrt(result)
            print(f"    Standard Deviation of the amount of small bags of avocados sold over a 4 year period : {str(round(standard_deviation, 3))}\n")

        ### Sub-menu-2 Option 3
        elif command_two == "3":
            average = sum(list_large_bags) / len(list_large_bags)
            value_minus_average = [(x - average) ** 2 for x in list_large_bags]
            result = sum(list_large_bags) / (len(list_large_bags) - 1)
            standard_deviation = math.sqrt(result)
            print(f"    Standard Deviation of the amount of large bag of avocados sold over a 4 year period : {str(round(standard_deviation, 3))}\n")

        ### Sub-menu-2 Option 4
        elif command_two == "4":
            average = sum(list_xlarge_bags) / len(list_xlarge_bags)
            value_minus_average = [(x - average) ** 2 for x in list_xlarge_bags]
            result = sum(list_xlarge_bags) / (len(list_xlarge_bags) - 1)
            standard_deviation = math.sqrt(result)
            print(f"    Standard Deviation of the amount of X-large bag of avocados sold over a 4 year period : {str(round(standard_deviation, 3))}\n")

        ### Sub-menu-2 Option invalid
        else:
            print(f"    {command_two} is an invalid selection")


    ### if the user chooses 4 from the main menu...
    elif command == "4":

        ### Show the user the Sub-menu-3
        command_three = input(
            "   Get the correlation between Average avocado price & another variable\n"
            "   Please enter a number corresponding to the instruction : \n"
            "   1 - Get the correlation between Average avocado price & Total Volume of avocados sold\n"
            "   2 - Get the correlation between Average avocado price & Small Bags of avocados sold  \n"
            "   3 - Get the correlation between Average avocado price & Large Bags of avocados sold \n"
            "   4 - Get the correlation between Average avocado price & X Large Bags of avocados sold  \n"
        )

        with open("./log.txt", "a") as log_file:
            log_file.write(f"The user has chosen sub-option : '{command_three}' from the sub-menu \n")
            log_file.close()

        ### Sub-menu-3 Option 1
        if command_three == "1":
            # Top line
            average_x = sum(list_average_price) / len(list_average_price)
            average_y = sum(list_total_volume) / len(list_total_volume)

            deviations_for_x = [x - average_x for x in list_average_price]
            deviations_for_y = [y - average_y for y in list_total_volume]

            # For multiplying corrosponding values in the two lists
            deviations_for_xy = [x * y for (x, y) in zip(deviations_for_x, deviations_for_y)]

            deviations_for_x_squ = [(x - average_x) ** 2 for x in list_average_price]
            deviations_for_y_squ = [(y - average_y) ** 2 for y in list_total_volume]

            corralation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ)) * (sum(deviations_for_y_squ)))

            print(f"    Correlation between Average avocado price & Total Volume of avocados sold : { round(corralation, 3) }\n")

        ### Sub-menu-3 Option 2
        elif command_three == "2" :
            # Top line
            average_x = sum(list_average_price) / len(list_average_price)
            average_y = sum(list_small_bags) / len(list_small_bags)

            deviations_for_x = [x - average_x for x in list_average_price]
            deviations_for_y = [y - average_y for y in list_small_bags]

            # For multiplying corrosponding values in the two lists
            deviations_for_xy = [x * y for (x, y) in zip(deviations_for_x, deviations_for_y)]

            deviations_for_x_squ = [(x - average_x) ** 2 for x in list_average_price]
            deviations_for_y_squ = [(y - average_y) ** 2 for y in list_small_bags]

            corralation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ)) * (sum(deviations_for_y_squ)))

            print(f"    Correlation between Average avocado price & Small Bags of avocados sold : {round(corralation, 3)}\n")

        ### Sub-menu-3 Option 3
        elif command_three == "3":
            # Top line
            average_x = sum(list_average_price) / len(list_average_price)
            average_y = sum(list_large_bags) / len(list_large_bags)

            deviations_for_x = [x - average_x for x in list_average_price]
            deviations_for_y = [y - average_y for y in list_large_bags]

            # For multiplying corrosponding values in the two lists
            deviations_for_xy = [x * y for (x, y) in zip(deviations_for_x, deviations_for_y)]

            deviations_for_x_squ = [(x - average_x) ** 2 for x in list_average_price]
            deviations_for_y_squ = [(y - average_y) ** 2 for y in list_large_bags]

            corralation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ)) * (sum(deviations_for_y_squ)))

            print(f"    Correlation between Average avocado price & Large Bags of avocados sold  : {round(corralation, 3)}\n")

        ### Sub-menu-3 Option 4
        elif command_three == "4":
            # Top line
            average_x = sum(list_average_price) / len(list_average_price)
            average_y = sum(list_xlarge_bags) / len(list_xlarge_bags)

            deviations_for_x = [x - average_x for x in list_average_price]
            deviations_for_y = [y - average_y for y in list_xlarge_bags]

            # For multiplying corrosponding values in the two lists
            deviations_for_xy = [x * y for (x, y) in zip(deviations_for_x, deviations_for_y)]

            deviations_for_x_squ = [(x - average_x) ** 2 for x in list_average_price]
            deviations_for_y_squ = [(y - average_y) ** 2 for y in list_xlarge_bags]

            corralation = sum(deviations_for_xy) / math.sqrt((sum(deviations_for_x_squ)) * (sum(deviations_for_y_squ)))

            print(f"    Correlation between Average avocado price & X Large Bags of avocados sold : {round(corralation, 3)}\n")

        ### Sub-menu-3 Option invalid
        else :
            print(f"    {command_three} is an invalid selection \n")

            with open("./log.txt", "a") as log_file:
                log_file.write(f"The user has invalid option : '{command}' from the sub menu \n")
                log_file.close()


    ### if the user chooses 1 from the main menu...
    elif command == "1":
        print(f"    There are {line_count} unique lines in the file")
        print(f"    The Max/Min Average price of an individual avocado: €{min(list_average_price)} / €{max(list_average_price)}")
        print(f"    The Max/Min sale amount of a small avocado bag : {min(list_small_bags)} / {max(list_small_bags)} ")
        print(f"    The Max/Min sale amount of a large avocado bag : {min(list_large_bags)} / {max(list_large_bags)} ")
        print(f"    The Max/Min sale amount of a X-large small avocado bag : {min(list_xlarge_bags)} / {max(list_xlarge_bags)} \n")




    ### if the user chooses an invalid option from the main menu...
    else:
        print("Please enter a valid command\n")
        with open("./log.txt", "a") as log_file:
            log_file.write(f"The user has chosen an invalid option : '{command} from the main menu \n")
            log_file.close()




    ### The user has reached the end of the program, offer the option begin again...
    continue_command = input("Press any key begin again or Q to quit\n")

    print(" ")

    ### The user has opted to Quit...
    if continue_command.upper() == "Q":

        command = "Q"
        with open("./log.txt", "a") as log_file:
            log_file.write(f"File analysis has ended - The user has entered : '{continue_command}' and opted to terminate the program \n")
            log_file.close()

    ### The user opted to start again...
    else:

        with open("./log.txt", "a") as log_file:
            log_file.write(f"File analysis has ended - The user has entered : '{continue_command}' and opted to run the program again \n")
            log_file.close()

print("The application has ended.")

with open("./log.txt", "a") as log_file:
    log_file.write(f"The application has ended \n")
    log_file.close()