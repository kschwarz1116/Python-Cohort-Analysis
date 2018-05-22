"""
Imports the list of orders
"""

from typing import Dict, List
import csv
import datetime as dt

from customer import *

def read_orders(order_file: str, customers: Dict[int, Customer]) -> Dict[int, Customer]:
    """
    """

    with open(order_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num = 0 # type: int
        for row in csv_reader:
            if row_num != 0:
                customers = read_order(customers, int(row[2]), row[3])
            row_num += 1

    return customers

def read_order(customers: Dict[int, Customer], customer: int, order: str) -> Dict[int, Customer]:
    if customer in customers:
        try:
            parse_order = dt.datetime.strptime(order, "%Y-%m-%d %H:%M:%S") # type: dt.datetime
        except ValueError:
            #Don't import the line for a ValueError
            pass
        else:
            customers[customer].order_times.append(parse_order)
    return customers
