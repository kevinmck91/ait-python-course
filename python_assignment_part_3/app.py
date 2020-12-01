# A00679670

import math
from python_assignment_part_3.utilities import file_IO_utils
from python_assignment_part_3.utilities import stats_utils
from python_assignment_part_3.utilities import graph_utils

file_path = "avocado.csv"

with open("./log.txt", "a") as log_file:
    log_file.write(f"\n***** The Application has been initialised ******  \n")
    log_file.close()


type_list = file_IO_utils.parse_file("./avocado.csv", "type")
volume_list = file_IO_utils.parse_file("./avocado.csv", "total_volume")
total_bags_list = file_IO_utils.parse_file("./avocado.csv", "total_bags")
region_list = file_IO_utils.parse_file("./avocado.csv", "list_region")
year_list = file_IO_utils.parse_file("./avocado.csv", "year")

### PIE CHARTS ###

#name1 = "Volume of Avocados Sold by Type"
#graph_utils.generate_pie_chart(type_list,volume_list, name1)

#name2 = "Volume of Bags of Avocados Sold by Type"
#graph_utils.generate_pie_chart(type_list,total_bags_list, name2)

#name3 = "Volume of Avocados Sold by year"
#graph_utils.generate_pie_chart(year_list,volume_list, name3)

#name4 = "Volume of Avocados Sold by Region"
#graph_utils.generate_pie_chart(region_list,volume_list, name4)


### BAR CHARTS ###

graph_utils.generate_barchart(region_list, volume_list)
#graph_utils.generate_barchart(type_list,total_bags_list)
graph_utils.generate_barchart(year_list,volume_list)

