"""
Test file for write_analysis.py
"""
import datetime as dt

from customer import Customer
import write_analysis as write

def test_1() -> None:
    """
    get_created_date]
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
    add_to_cohorts
    """

def test_3() -> None:
    """
    generate_cohort_analysis
    """
