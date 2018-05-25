"""
This script holds the main functionality for the Cohort Analysis programming challenge.
"""

import sys

from customer import CUSTOMERS
import read_customer
import read_orders
import write_analysis as write

def main() -> None:
    """This function accepts command line arguments and parses them into a table"""

    num_args: int = len(sys.argv)
    if (num_args < 4) or (num_args > 6):
        print("Got improper args")
        return

    customer_file: str = sys.argv[1]
    order_file: str = sys.argv[2]
    out_file: str = sys.argv[3]
    offset_hours: str = sys.argv[4]

    customers: CUSTOMERS = read_customer.read_customers(customer_file)
    read_orders.read_orders(order_file, customers)

    write.print_cohort_analysis(write.generate_cohort_analysis(customers, offset_hours), out_file)

main()
