"""
Test file for read_customer.py
"""

import datetime as dt

from customer import Customer, CUSTOMERS
import read_customer

def test_1() -> None:
    """
    Ensure we fail on bad input strings
    """
    customers: CUSTOMERS = {}
    read_customer.read_customer(customers, 0, "")
    assert customers == {}

    read_customer.read_customer(customers, 0, "1")
    assert customers == {}

def test_2() -> None:
    """
    Ensure we can add individual customers
    """
    customers: CUSTOMERS = {}
    read_customer.read_customer(customers, 0, "2018-01-01 12:00:00")

    customers0: CUSTOMERS = {}
    customers0[0] = Customer(dt.datetime(2018, 1, 1, 12, 0, 0))

    assert customers_equiv(customers, customers0)

    read_customer.read_customer(customers, 1, "2018-01-31 05:00:00")
    customers0[1] = Customer(dt.datetime(2018, 1, 31, 5, 0, 0))

    assert customers_equiv(customers, customers0)

def test_3() -> None:
    """
    Ensure we can load files
    """

def customers_equiv(customers0: CUSTOMERS, customers1: CUSTOMERS) -> bool:
    """
    Compares two CUSTOMERS dicts for equivalency
    """
    if len(customers0) == len(customers1):
        customer_id: int
        for customer_id in customers0:
            if not customer_equiv(customers0[customer_id], customers1[customer_id]):
                return False
        return True
    return False

def customer_equiv(customer0: Customer, customer1: Customer) -> bool:
    """
    Compares two customers for equivalency (not checking order_times)
    """
    return customer0.created == customer1.created
