"""
Organizes the customer hashtable into a printable format, and prints to csv
"""

from typing import Dict, List, Tuple
import csv
import datetime as dt

from customer import *


def generate_cohort_analysis(customers: Dict[int, Customer], offset: str) -> List[Tuple[dt.date, int, List[int]]]:
    """
    Returns a list of (datetime, number of customers, [distinct purchases])
    datetime represents end time of a cohort
    number of customers represent customers in that cohort
    [distinct purchases] is a list where index n is equal to the number of
    distinct customers that made a purchase within the nth week of their signup
    """
    cohorts = [] # type: List[Tuple[dt.date, int, List[int]]]
    timezone = dt.timezone(dt.timedelta(hours = float(offset))) # type: dt.timezone

    #Find cohort bounds - defined based on earliest and latest dates in the correct timezone
    earliest_created = get_created_date_from_customer(customers[min(customers, key=lambda x: customers[x].created)], timezone)
    latest_created = get_created_date_from_customer(customers[max(customers, key=lambda x: customers[x].created)], timezone)

    #Initialize output array
    cohort = latest_created
    while earliest_created <= cohort:
        cohorts.append((cohort, 0, []))
        cohort = cohort - dt.timedelta(7)
    
    for customer in customers.values():
        add_to_cohorts(customer, cohorts, timezone)

    return cohorts

def get_created_date_from_customer(customer: Customer, timezone: dt.timezone) -> dt.date:
    created_time = customer.created
    return created_time.astimezone(timezone).date()

def add_to_cohorts(customer: Customer, cohorts: List[Tuple[dt.date, int, List[int]]], timezone: dt.timezone) -> None:
    cohort = (cohorts[0][0] - get_created_date_from_customer(customer, timezone)) // dt.timedelta(7)

    date, num_customers, distinct_purchases = cohorts[cohort]
    
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
    
    cohorts[cohort] = (date, num_customers, distinct_purchases)
    return

def print_cohort_analysis(cohorts: List[Tuple[dt.date, int, List[int]]], out_file: str) -> None:
    num_weeks = len(max(cohorts, key=lambda x: len(x[2]))[2])

    with open(out_file, 'w', newline='') as csvfile:
        cohort_writer = csv.writer(csvfile, delimiter=',')
        cohort_writer.writerow(["Cohort", "Customers"] + list(map(lambda x: str(7*x) + "-" + str(7*x+6) + " days", range(num_weeks))))
        cohort_writer.writerows(map(flatten_tuple , cohorts))

    return

def flatten_tuple(tup):
    end_time, num_customers, list_purchases = tup
    return [str(end_time - dt.timedelta(6)) + " - " +  str(end_time), num_customers] + list_purchases
