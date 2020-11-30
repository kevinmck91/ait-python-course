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
region_list = file_IO_utils.parse_file("./avocado.csv", "list_region")

#graph_utils.generate_pie_chart(type_list)
#graph_utils.generate_pie_chart(region_list)

graph_utils.generate_barchart_single(region_list)

