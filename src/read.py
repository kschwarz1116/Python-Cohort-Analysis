"""
Imports the list of customers
"""

from typing import Dict
import csv
import customer
import datetime

def import_customers(customer_file: str) -> Dict[int, customer.Customer]:
    """This functions takes in a file name and
    outputs a dictionary containing the file's customers"""
    ht = {} # type: Dict[int, customer.Customer]
    with open(customer_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num = 0 # type: int
        for row in csv_reader:
            if row_num != 0:            
                ht[int(row[0])] = customer.Customer(parse_datetime(row[1]))
            row_num += 1
    return ht

def parse_datetime(datetime_string: str) -> datetime.datetime:
    return datetime.datetime.now()
