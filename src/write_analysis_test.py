"""
Test file for write_analysis.py
"""
import datetime as dt

from customer import Customer
import write_analysis as write
from read_customer import read_customer

def test_1() -> None:
    """
    get_created_date
    """
    customer: Customer = Customer(dt.datetime(2018, 1, 1, 0, 0, 0, tzinfo=dt.timezone.utc))
    tzone: dt.timezone = dt.timezone(dt.timedelta(hours=0))
    assert write.get_created_date(customer, tzone) == dt.date(2018, 1, 1)

    tzone = dt.timezone(dt.timedelta(hours=1))
    assert write.get_created_date(customer, tzone) == dt.date(2018, 1, 1)

    tzone = dt.timezone(dt.timedelta(hours=-1))
    assert write.get_created_date(customer, tzone) == dt.date(2017, 12, 31)

def test_2() -> None:
    """
    generate_cohorts
    """
    timezone0: dt.timezone = dt.timezone(dt.timedelta(hours=0))
    timezone_back2: dt.timezone = dt.timezone(dt.timedelta(hours=-2))

    customers = {}
    cohorts: write.CSVARRAY = write.generate_cohorts(customers, timezone0)
    assert cohorts == []

    read_customer(customers, 0, "2018-01-01 00:01:00")
    cohorts = write.generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 0, [])]

    cohorts = write.generate_cohorts(customers, timezone_back2)
    assert cohorts == [(dt.date(2017, 12, 31), 0, [])]

    read_customer(customers, 1, "2018-01-01 00:01:00")
    cohorts = write.generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 1), 0, [])]

    read_customer(customers, 1, "2018-01-07 12:01:00")
    cohorts = write.generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 7), 0, [])]

    read_customer(customers, 1, "2018-01-07 12:01:00")
    cohorts = write.generate_cohorts(customers, timezone_back2)
    assert cohorts == [(dt.date(2018, 1, 7), 0, []), (dt.date(2017, 12, 31), 0, [])]

    read_customer(customers, 1, "2018-01-20 12:01:00")
    cohorts = write.generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 20), 0, []), (dt.date(2018, 1, 13), 0, []), (dt.date(2018, 1, 6), 0, [])]

    read_customer(customers, 2, "2018-01-08 12:01:00")
    cohorts = write.generate_cohorts(customers, timezone0)
    assert cohorts == [(dt.date(2018, 1, 20), 0, []), (dt.date(2018, 1, 13), 0, []), (dt.date(2018, 1, 6), 0, [])]
    

def test_3() -> None:
    """
    add_to_cohorts
    """

def test_4() -> None:
    """
    generate_cohort_analysis
    """
