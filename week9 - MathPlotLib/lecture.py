# -*- coding: utf-8 -*-
"""
Program to visualise Trolley Watch data
Example of: matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)
"""
import datetime
import matplotlib.pyplot as plt


def get_data(filename):
    """
    Function to retrieve trolleywatch data from the file

    Parameters
    ----------
    filename : string
        The pathname of the file containing the data.

    Returns
    -------
    dates_data : dict
        A dictionary containing as key-value pairs the dates and the number of patients on that date
    hospitals_data : dict
        A dictionary containing as key-value pairs the hospital and the number of patients in that hospital.
    regions_data : dict
        A dictionary containing as key-value pairs the region and the number of patients in that region.
    trolley_vs_ward_numbers: list
        A list of tuples containing the trolley numbers and ward numbers.
    """
    # create empty dictionaries for the data
    dates_data = {}
    hospitals_data = {}
    regions_data = {}

    # create an empty list for the trolley and ward numbers
    trolley_vs_ward_numbers = []

    # date format string
    format_str = "%d/%m/%Y"

    # read the data from the file
    with open(filename) as datafile:
        # read the first line containing the headings and discard it
        datafile.readline()

        # for each other line in the file
        for line in datafile:
            # split the line into the components
            date_string, hospital, region, trolley, ward, patients = line.strip().split(",")

            # convert the date string to a datetime object
            date = datetime.datetime.strptime(date_string, format_str)

            # convert the patient value to an int, save having to code this repeatedly
            patients = int(patients)

            # if this is the first occurrence of this date
            if date not in dates_data:
                # insert into dictionary
                dates_data[date] = patients
            else:
                dates_data[date] += patients

            # if this is the first occurrence of this hospital
            if hospital not in hospitals_data:
                # insert into dictionary
                hospitals_data[hospital] = patients
            else:
                hospitals_data[hospital] += patients

                # if this is the first occurrence of this region
            if region not in regions_data:
                # insert into dictionary
                regions_data[region] = patients
            else:
                regions_data[region] += patients

                # add the trolley and ward numbers to a list of tuples
            trolley_vs_ward_numbers.append((int(trolley), int(ward)))

    # return the data structures for use with with matplotlib
    return dates_data, hospitals_data, regions_data, trolley_vs_ward_numbers
