"""
Test file for read_orders.py
"""

import datetime as dt

from customer import CUSTOMERS
from read_customer import read_customer
from read_orders import read_order
from test_equivalency import customers_equiv

def test_1() -> None:
    """
    Ensure we fail on bad input strings
    """
    customers_ex: CUSTOMERS = {}
    read_customer(customers_ex, 0, "2018-01-01 12:00:00")

    customers_act: CUSTOMERS = {}
    read_customer(customers_act, 0, "2018-01-01 12:00:00")

    read_order(customers_act, 0, "")
    assert customers_equiv(customers_ex, customers_act)

    read_order(customers_act, 0, "1")
    assert customers_equiv(customers_ex, customers_act)

def test_2() -> None:
    """
    Ensure we fail on bad customer_ids
    """
    customers_ex: CUSTOMERS = {}
    read_customer(customers_ex, 0, "2018-01-01 12:00:00")

    customers_act: CUSTOMERS = {}
    read_customer(customers_act, 0, "2018-01-01 12:00:00")

    read_order(customers_act, 1, "2018-01-01 12:00:00")
    assert customers_equiv(customers_ex, customers_act)

def test_3() -> None:
    """
    Ensure we add properly formatted orders
    """
    customers_ex: CUSTOMERS = {}
    customers_act: CUSTOMERS = {}

    read_customer(customers_ex, 0, "2018-01-01 12:00:00")
    read_customer(customers_act, 0, "2018-01-01 12:00:00")

    customers_ex[0].order_times.append(dt.datetime(2018, 1, 1, 12, 30, 0, tzinfo=dt.timezone.utc))
    read_order(customers_act, 0, "2018-01-01 12:30:00")
    assert customers_equiv(customers_ex, customers_act)

    customers_ex[0].order_times.append(dt.datetime(2018, 2, 1, 12, 14, 0, tzinfo=dt.timezone.utc))
    read_order(customers_act, 0, "2018-02-01 12:14:00")
    assert customers_equiv(customers_ex, customers_act)

    customers_ex[0].order_times.append(dt.datetime(2018, 3, 14, 15, 9, 26, tzinfo=dt.timezone.utc))
    read_order(customers_act, 0, "2018-03-14 15:09:26")
    assert customers_equiv(customers_ex, customers_act)

    read_customer(customers_ex, 1, "2017-01-03 3:00:00")
    read_customer(customers_act, 1, "2017-01-03 3:00:00")

    customers_ex[1].order_times.append(dt.datetime(2017, 6, 15, 3, 0, 0, tzinfo=dt.timezone.utc))
    read_order(customers_act, 1, "2017-06-15 3:00:00")
    assert customers_equiv(customers_ex, customers_act)

    customers_ex[1].order_times.append(dt.datetime(2017, 9, 15, 3, 0, 0, tzinfo=dt.timezone.utc))
    read_order(customers_act, 1, "2017-09-15 3:00:00")
    assert customers_equiv(customers_ex, customers_act)
