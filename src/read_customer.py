"""
Imports the list of customers
"""

from typing import Dict
import csv
import datetime as dt

from customer import *

def read_customers(customer_file: str) -> Dict[int, Customer]:
    """
    This function takes in a file name and
    outputs a dictionary containing the file's customers
    """

    customers = {} # type: Dict[int, Customer]
    with open(customer_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num = 0 # type: int
        for row in csv_reader:
            if row_num != 0:
                read_customer(customers, int(row[0]), row[1])
            row_num += 1
    return customers

def read_customer(customers: Dict[int, Customer], customer: int, created: str) -> Dict[int, Customer]:
    try:
        parse_created = dt.datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        #Don't import the line for a ValueError
        pass
    else:
        customers[customer] = Customer(parse_created)    
    return customers
