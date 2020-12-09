# A00679670

import math
from python_assignment_part_3.utilities import file_IO_utils
from python_assignment_part_3.utilities import stats_utils
from python_assignment_part_3.utilities import graph_utils

file_path = "./avocado.csv"

# Call File IO to get a specific Graph for data analysis
type_list       = file_IO_utils.parse_file(file_path, "type")
region_list     = file_IO_utils.parse_file(file_path, "list_region")
year_list       = file_IO_utils.parse_file(file_path, "year")

date_list       = file_IO_utils.parse_file(file_path, "date")

volume_list     = file_IO_utils.parse_file(file_path, "total_volume")
total_bags_list = file_IO_utils.parse_file(file_path, "total_bags")
small_bags_list = file_IO_utils.parse_file(file_path, "small_bags")
large_bags_list = file_IO_utils.parse_file(file_path, "large_bags")

### This section analyzes the file depending on user input on a Main Menu and Sub Menu Basis

command = ""

while command != "Q":

    ### This section provides the user to choose an value off the Main menu
    command = input(
        "\n\nPlease enter a command : \n"
        "1 - Generate a graphical outputs from the data \n"
        "2 - Generate a file with statistics from the data \n"
        "Q - Exit / Quit\n"
        "-------> "
    ).upper()

    if command == "Q":
        print(f"Program is exiting.\n")
        break

    # if the user chooses 1 from the main menu...
    elif command == "1":

        command_one = input(
            "   Generate Graphical data\n"
            "   Please enter a number corresponding to the instruction : \n"
            "   1 - Output set of line graphs from data\n"
            "   2 - Output set of Pie Chart\n"
            "   3 - Output set of Bar Chart\n"
            "   4 - Output set of Box Plot\n"
            "   5 - Output Bar Charts of Multiple Box Plot\n"
            "------->"
        )

        if command_one == "1":

            graph_utils.generate_date_line_chart(date_list, volume_list, name="Volume of Avocado sold over time", x_label="Time", y_label="Volume of Avocado sold")
            graph_utils.generate_date_line_chart(date_list, total_bags_list, name="Volume of bags of Avocado sold over time", x_label="Time", y_label="Volume of bags of Avocado sold")
            graph_utils.generate_date_line_chart(date_list, small_bags_list, name="Volume of small bags of Avocado sold over time", x_label="Time", y_label="Volume of small bags of  Avocado sold")
            graph_utils.generate_date_line_chart(date_list, large_bags_list, name="Volume of large bags of Avocado sold over time", x_label="Time", y_label="Volume of large bags of Avocado sold")

        elif command_one == "2":

            graph_utils.generate_category_figure_pie_chart(type_list,volume_list, name="Volume of Avocados sold grouped by type")
            graph_utils.generate_category_figure_pie_chart(type_list, total_bags_list, name="Volume of bags of Avocado sold grouped by type" )
            graph_utils.generate_category_figure_pie_chart(year_list, small_bags_list, name="Volume of small bags of Avocado sold grouped by year")
            graph_utils.generate_category_figure_pie_chart(year_list, large_bags_list, name="Volume of large bags of Avocado sold grouped by year")

        elif command_one == "3":

            graph_utils.generate_category_figure_barchart(region_list, volume_list,  name="Volume of Avocados sold grouped by region", x_label="Volume", y_label="Regions")
            graph_utils.generate_category_figure_barchart(region_list, total_bags_list, name="Volume of bags of Avocados sold grouped by region", x_label="Volume", y_label="Regions")
            graph_utils.generate_category_figure_barchart(type_list,volume_list,  name="Volume of Avocados sold grouped by type", x_label="Volume", y_label="type")
            graph_utils.generate_category_figure_barchart(type_list, small_bags_list,  name="Volume of small bags of Avocados sold grouped by type", x_label="Volume", y_label="type")
            graph_utils.generate_category_figure_barchart(year_list,volume_list, name="Volume of Avocados sold grouped by year", x_label="Volume", y_label="Year")
            graph_utils.generate_category_figure_barchart(year_list, large_bags_list, name="Volume of large bags of Avocados sold grouped by year", x_label="Volume", y_label="Year")

        elif command_one == "4":

            graph_utils.generate_category_figure_boxplot(type_list, volume_list, category_identifier="organic", name="Box Plot of organic Avocados sold by volume", x_label="Organic Avocado", y_label="Volume")
            graph_utils.generate_category_figure_boxplot(type_list, volume_list, category_identifier="conventional", name="Box Plot of conventional Avocados sold by volume", x_label="Conventional Avocado", y_label="Volume")

        elif command_one == "5":
            print("Generating graphs, Please wait...")
            graph_utils.generate_barchart_boxplot(year_list,volume_list, name="Box plot of volumes sold by year", x_label="Volume", y_label="Year")
            graph_utils.generate_barchart_boxplot(type_list, volume_list, name="Box plot of volumes sold by type", x_label="Volume", y_label="Type")

        else:
            print(f"{command_one} is an invalid selection \n")
            print(f"Program is exiting. Please Run again \n")
            command = 'Q'

    elif command == "2":

        print(f"Generating file, please wait.. \n")

        with open("./stats.txt", "w") as stats_file:
            stats_file.write(f"Here are the statistics for the application \n")

            stats_file.write(f"Mean - Total Volume Sold: {stats_utils.get_mean(volume_list)} \n")
            stats_file.write(f"Median - Total Volume Sold: {stats_utils.get_median(volume_list)} \n")
            stats_file.write(f"Mode - Total Volume Sold: {stats_utils.get_mode(volume_list)} \n")
            stats_file.write(f"Standard Deviation - Total Volume Sold: {stats_utils.get_standard_deviation(volume_list)} \n")

            stats_file.write(f"Mean - Total Bags Sold: {stats_utils.get_mean(total_bags_list)} \n")
            stats_file.write(f"Median - Total Bags Sold: {stats_utils.get_median(total_bags_list)} \n")
            stats_file.write(f"Mode - Total Bags Sold: {stats_utils.get_mode(total_bags_list)} \n")
            stats_file.write(f"Standard Deviation - Total Bags Sold: {stats_utils.get_standard_deviation(total_bags_list)} \n")

            stats_file.write(f"Mean - Large bags sold: {stats_utils.get_mean(large_bags_list)} \n")
            stats_file.write(f"Median - Large bags sold : {stats_utils.get_median(large_bags_list)} \n")
            stats_file.write(f"Mode - Large bags sold: {stats_utils.get_mode(large_bags_list)} \n")
            stats_file.write(f"Standard Deviation - Large bags sold : {stats_utils.get_standard_deviation(large_bags_list)} \n")

            stats_file.write(f"Correlation between Total Volume Sold and Total Bags Sold : {stats_utils.get_correlation(volume_list, total_bags_list)} \n")
            stats_file.write(f"Correlation between Total Volume Sold and Large bags sold : {stats_utils.get_correlation(volume_list, large_bags_list)}\n")
            stats_file.write(f"Correlation between Total Bags Sold and Large bags sold : {stats_utils.get_correlation(total_bags_list, large_bags_list)} \n")

            stats_file.close()

            print(f"\'stats.txt\' has been saved in the root folder")

    else:
        print(f"{command} is an invalid selection \n")
        print(f"Program is exiting. Please Run again \n")
        command = 'Q'





