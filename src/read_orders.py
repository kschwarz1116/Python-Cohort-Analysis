"""
Imports the list of orders
"""

import csv
import datetime as dt

from customer import CUSTOMERS

def read_orders(order_file: str, customers: CUSTOMERS) -> None:
    """
    Reads in the orders file, modifying the CUSTOMERS Dict
    """

    with open(order_file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        row_num: int = 0
        for row in csv_reader:
            if row_num != 0:
                read_order(customers, int(row[2]), row[3])
            row_num += 1

def read_order(customers: CUSTOMERS, customer_id: int, order: str) -> None:
    """
    Reads in an individual customer order, poorly formatted orders are ignored.
    """
    if customer_id in customers:
        try:
            parse_order: dt.datetime = dt.datetime.strptime(order, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            #Don't import the line for a ValueError
            pass
        else:
            customers[customer_id].order_times.append(parse_order)
