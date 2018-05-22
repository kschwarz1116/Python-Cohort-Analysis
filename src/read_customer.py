"""
Imports the list of customers
"""

from typing import Dict
import csv
import datetime

import customer

def import_customers(customer_file: str) -> Dict[int, customer.Customer]:
    """
    This function takes in a file name and
    outputs a dictionary containing the file's customers
    """

    customers = {} # type: Dict[int, customer.Customer]
    with open(customer_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num = 0 # type: int
        for row in csv_reader:
            if row_num != 0:
                try:
                    parse_result = parse_datetime(row[1])
                except ValueError:
                    #Don't import the line for a ValueError
                    pass
                else:
                    customers[int(row[0])] = customer.Customer(parse_result)
            row_num += 1
    return customers

def parse_datetime(datetime_string: str) -> datetime.datetime:
    """
    Parses a string into a datetime object.
    Raises ValueError for invalid strings.
    """
    try:
        datetime_out = datetime.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise
    return datetime_out
