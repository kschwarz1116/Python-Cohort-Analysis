"""
Imports the list of customers
"""

from typing import Dict
import csv
import datetime as dt

from customer import Customer, CUSTOMERS

def read_customers(customer_file: str) -> Dict[int, Customer]:
    """
    This function takes in a file name and
    outputs a dictionary containing the file's customers
    """

    customers: CUSTOMERS = {}
    with open(customer_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num: int = 0
        for row in csv_reader:
            if row_num != 0:
                read_customer(customers, int(row[0]), row[1])
            row_num += 1
    return customers

def read_customer(customers: CUSTOMERS, customer: int, created: str) -> None:
    """
    Attempts to create a customer. Creation times with bad formatting are ignored.
    """
    try:
        created_dt: dt.datetime = dt.datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
        created_dt = dt.datetime.combine(created_dt.date(), created_dt.time(), dt.timezone.utc)
    except ValueError:
        #Don't import the line for a ValueError
        pass
    else:
        customers[customer] = Customer(created_dt)
