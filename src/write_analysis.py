"""
Organizes the customer hashtable into a printable format, and prints to csv
"""

from typing import Callable, List, Set, Tuple
import csv
import datetime as dt

from customer import Customer, CUSTOMERS

CSVARRAY = List[Tuple[dt.date, int, List[int]]]

def generate_cohort_analysis(customers: CUSTOMERS, offset: str) -> CSVARRAY:
    """
    Returns a list of (datetime, number of customers, [distinct purchases])
    datetime represents end time of a cohort
    number of customers represent customers in that cohort
    [distinct purchases] is a list where index n is equal to the number of
    distinct customers that made a purchase within the nth week of their signup
    """
    tzone: dt.timezone = dt.timezone(dt.timedelta(hours=float(offset)))
    cohorts: CSVARRAY = generate_cohorts(customers, tzone)

    for customer in customers.values():
        add_to_cohorts(customer, cohorts, tzone)

    return cohorts

def generate_cohorts(customers: CUSTOMERS, tzone: dt.timezone) -> CSVARRAY:
    """
    Initializes the cohorts array based on the creation dates of customers
    """
    cohorts: CSVARRAY = []

    if customers:
        #Find cohort bounds - defined based on earliest and latest dates in the correct timezone
        get_created: Callable[[int], dt.datetime] = lambda x: customers[x].created
        earliest_date: dt.date = get_created_date(customers[min(customers, key=get_created)], tzone)
        latest_date: dt.date = get_created_date(customers[max(customers, key=get_created)], tzone)

        #Initialize output array
        cohort: dt.date = latest_date
        while earliest_date <= cohort:
            cohorts.append((cohort, 0, []))
            cohort = cohort - dt.timedelta(7)

    return cohorts

def get_created_date(customer: Customer, tzone: dt.timezone) -> dt.date:
    """
    Given a customer, returns their created date, localized to timezone
    """
    created_time: dt.datetime = customer.created
    return created_time.astimezone(tzone).date()

def add_to_cohorts(customer: Customer, cohorts: CSVARRAY, tzone: dt.timezone) -> None:
    """
    Given a customer, adds them to the cohorts array based on their created time and purchases
    """
    cohort_index: int = (cohorts[0][0] - get_created_date(customer, tzone)) // dt.timedelta(7)

    date: dt.date
    num_customers: int
    distinct_purchases: List[int]
    date, num_customers, distinct_purchases = cohorts[cohort_index]

    num_customers += 1

    distinct_purchase_weeks: Set[int] = set()
    max_purchase_week: int = -1
    purchase_week: int

    for time in customer.order_times:
        purchase_week = (time - customer.created) // dt.timedelta(7)
        distinct_purchase_weeks.add(purchase_week)
        max_purchase_week = max(max_purchase_week, purchase_week)

    if len(distinct_purchases) < max_purchase_week + 1:
        distinct_purchases.extend([0]*(max_purchase_week + 1 - len(distinct_purchases)))

    for purchase_week in distinct_purchase_weeks:
        cohorts[cohort_index][2][purchase_week] += 1

    cohorts[cohort_index] = (date, num_customers, distinct_purchases)

def print_cohort_analysis(cohorts: CSVARRAY, out_file: str) -> None:
    """
    Generates the CSV for cohorts into out_file
    """
    num_weeks: int = len(max(cohorts, key=lambda x: len(x[2]))[2])

    with open(out_file, 'w', newline='') as csvfile:
        cohort_writer = csv.writer(csvfile, delimiter=',')
        cohort_bounds: Callable[[int], str] = lambda x: str(7*x) + "-" + str(7*x+6) + " days"
        day_headers: List[str] = list(map(cohort_bounds, range(num_weeks)))
        cohort_writer.writerow(["Cohort", "Customers"] + day_headers)
        cohort_writer.writerows(map(format_tuple, cohorts))

    return

def format_tuple(tup):
    """
    Prepares tuple for writerows so that each element is separated by a comma
    Not typing this one. See mypy issue #3935
    """
    end_date, num_customers, purchase_list = tup
    return [str(end_date - dt.timedelta(6)) + " - " +  str(end_date), num_customers] + purchase_list
