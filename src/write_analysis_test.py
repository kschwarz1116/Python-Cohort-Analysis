"""
Test file for write_analysis.py
"""
import datetime as dt

from customer import Customer, CUSTOMERS
from write_analysis import CSVARRAY, get_created_date, generate_cohorts, add_to_cohorts
from read_customer import read_customer
from read_orders import read_order

timezone0: dt.timezone = dt.timezone(dt.timedelta(hours=0))
timezone_back2: dt.timezone = dt.timezone(dt.timedelta(hours=-2))



def test_1() -> None:
    """
    get_created_date
    """
    customer: Customer = Customer(dt.datetime(2018, 1, 1, 0, 0, 0, tzinfo=dt.timezone.utc))
    tzone: dt.timezone = dt.timezone(dt.timedelta(hours=0))
    assert get_created_date(customer, tzone) == dt.date(2018, 1, 1)

    tzone = dt.timezone(dt.timedelta(hours=1))
    assert get_created_date(customer, tzone) == dt.date(2018, 1, 1)

    tzone = dt.timezone(dt.timedelta(hours=-1))
    assert get_created_date(customer, tzone) == dt.date(2017, 12, 31)

def test_2() -> None:
    """
    generate_cohorts
    """

    customers: CUSTOMERS = {}
    cohorts: CSVARRAY = generate_cohorts(customers, timezone0)
    assert cohorts == []

    read_customer(customers, 0, "2018-01-01 00:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 0, [])]

    cohorts = generate_cohorts(customers, timezone_back2)
    assert cohorts == [(dt.date(2017, 12, 31), 0, [])]

    read_customer(customers, 1, "2018-01-01 00:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 0, [])]

    read_customer(customers, 1, "2018-01-07 12:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 7), 0, [])]

    read_customer(customers, 1, "2018-01-07 12:01:00")
    cohorts = generate_cohorts(customers, timezone_back2)
    assert cohorts == [(dt.date(2018, 1, 7), 0, []), (dt.date(2017, 12, 31), 0, [])]

    read_customer(customers, 1, "2018-01-20 12:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    assert cohorts == ([(dt.date(2018, 1, 20), 0, []),
                        (dt.date(2018, 1, 13), 0, []),
                        (dt.date(2018, 1, 6), 0, [])])

    read_customer(customers, 2, "2018-01-08 12:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    assert cohorts == ([(dt.date(2018, 1, 20), 0, []),
                        (dt.date(2018, 1, 13), 0, []),
                        (dt.date(2018, 1, 6), 0, [])])

def test_3() -> None:
    """
    add_to_cohorts
    """

    customers: CUSTOMERS = {}
    read_customer(customers, 0, "2018-01-01 00:01:00")
    cohorts: CSVARRAY = generate_cohorts(customers, timezone0)
    add_to_cohorts(customers[0], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 1, [])]

    read_order(customers, 0, "2018-01-03 12:01:00")
    cohorts = generate_cohorts(customers, timezone0)
    add_to_cohorts(customers[0], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 1, [1])]

    read_order(customers, 0, "2018-01-09 12:02:00")
    cohorts = generate_cohorts(customers, timezone0)
    add_to_cohorts(customers[0], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 1, [1, 1])]

    read_customer(customers, 1, "2017-12-30 12:01:00")
    read_order(customers, 1, "2018-01-10 11:00:00")
    add_to_cohorts(customers[1], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 2, [1, 2])]


    read_customer(customers, 1, "2018-01-07 12:00:00")
    read_order(customers, 1, "2018-01-20 12:00:00")
    cohorts = generate_cohorts(customers, timezone0)
    add_to_cohorts(customers[0], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 7), 1, [1, 1])]

    add_to_cohorts(customers[1], cohorts, timezone0)
    assert cohorts == [(dt.date(2018, 1, 7), 2, [1, 2])]

    cohorts = generate_cohorts(customers, timezone_back2)
    add_to_cohorts(customers[0], cohorts, timezone_back2)
    assert cohorts == [(dt.date(2018, 1, 7), 0, []), (dt.date(2017, 12, 31), 1, [1, 1])]

    add_to_cohorts(customers[1], cohorts, timezone_back2)
    assert cohorts == [(dt.date(2018, 1, 7), 1, [0, 1]), (dt.date(2017, 12, 31), 1, [1, 1])]
