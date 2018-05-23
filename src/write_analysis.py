"""
Organizes the customer hashtable into a printable format, and prints to csv
"""

from typing import Dict, List, Tuple
import csv
import datetime as dt

from customer import *


def generate_cohort_analysis(customers: Dict[int, Customer]) -> List[Tuple[dt.datetime, int, List[int]]]:
    """
    Returns a list of (datetime, number of customers, [distinct purchases])
    datetime represents end time of a cohort
    number of customers represent customers in that cohort
    [distinct purchases] is a list where index n is equal to the number of
    distinct customers that made a purchase within the nth week of their signup
    """
    cohorts = [] # type: List[Tuple[dt.datetime, int, List[int]]]

    #Find cohort bounds
    earliest_created = customers[min(customers, key=lambda x: customers[x].created)].created
    latest_created = customers[max(customers, key=lambda x: customers[x].created)].created

    #Initialize output array
    cohort = latest_created
    while earliest_created <= cohort:
        cohorts.append((cohort, 0, []))
        cohort = cohort - dt.timedelta(7)
    
    for customer in customers.values():
        add_to_cohorts(customer, cohorts)

    return cohorts

def add_to_cohorts(customer: Customer, cohorts: List[Tuple[dt.datetime, int, List[int]]]) -> None:
    cohort = (cohorts[0][0] - customer.created) // dt.timedelta(7)

    datetime, num_customers, distinct_purchases = cohorts[cohort]
    
    num_customers += 1

    distinct_purchase_weeks = set()
    max_purchase_week = 0

    for time in customer.order_times:
        purchase_week = (time - customer.created) // dt.timedelta(7)
        distinct_purchase_weeks.add(purchase_week)
        max_purchase_week = max(max_purchase_week, purchase_week)

    if (len(distinct_purchases) < max_purchase_week + 1):
        distinct_purchases.extend([0]*(max_purchase_week + 1 - len(distinct_purchases)))
    
    for purchase_week in distinct_purchase_weeks:
        cohorts[cohort][2][purchase_week] += 1

    
    cohorts[cohort] = (datetime, num_customers, distinct_purchases)
    return

def print_cohort_analysis(cohort: List[Tuple[dt.datetime, int, List[int]]], out_file: str) -> None:
    return
