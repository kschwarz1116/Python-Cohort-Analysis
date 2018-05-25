"""
Test file for read_customer.py
"""

import datetime as dt

from customer import Customer, CUSTOMERS
from read_customer import read_customer
from test_equivalency import customers_equiv

def test_1() -> None:
    """
    Ensure we fail on bad input strings
    """
    customers: CUSTOMERS = {}
    read_customer(customers, 0, "")
    assert customers == {}

    read_customer(customers, 0, "1")
    assert customers == {}

def test_2() -> None:
    """
    Ensure we can add individual customers
    """
    customers: CUSTOMERS = {}
    read_customer(customers, 0, "2018-01-01 12:00:00")

    customers0: CUSTOMERS = {}
    customers0[0] = Customer(dt.datetime(2018, 1, 1, 12, 0, 0, tzinfo=dt.timezone.utc))

    assert customers_equiv(customers, customers0)

    read_customer(customers, 1, "2018-01-31 05:00:00")
    customers0[1] = Customer(dt.datetime(2018, 1, 31, 5, 0, 0, tzinfo=dt.timezone.utc))

    assert customers_equiv(customers, customers0)
