# A00679670

import math
from python_assignment_part_3.utilities import file_IO_utils
from python_assignment_part_3.utilities import stats_utils

file_path = "avocado.csv"

with open("./log.txt", "a") as log_file:
    log_file.write(f"\n***** The Application has been initialised ******  \n")
    log_file.close()


total_volume_list = file_IO_utils.parse_file("./avocado.csv", "4225")


print(stats_utils.get_correlation())