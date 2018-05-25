"""
Creates equivalency functions for test routines
"""

from customer import Customer, CUSTOMERS

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
    Compares two customers for equivalency
    """
    return ((customer0.created == customer1.created) and
            (customer0.order_times == customer1.order_times))
