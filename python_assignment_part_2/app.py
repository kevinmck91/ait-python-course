# A00679670

import math
from python_assignment_part_2.utilities import file_IO_utils
file_path = "avocado.csv"

with open("./log.txt", "a") as log_file:
    log_file.write(f"\n***** The Application has been initialised ******  \n")
    log_file.close()


print(file_IO_utils.parse_file("./avocado.csv", "date"))
