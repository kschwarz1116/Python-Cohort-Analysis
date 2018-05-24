"""
This script holds the main functionality for the Cohort Analysis programming challenge.
"""

import sys
import read_customer
import read_orders
import write_analysis as write

def main() -> None:
    """This function accepts command line arguments and parses them into a table"""

    customer_file = "" # type: str
    order_file = "" # type: str
    num_args = len(sys.argv) # type: int
    if (num_args < 4) or (num_args > 6):
        print("Got improper args")
        return

    customer_file = sys.argv[1]
    order_file = sys.argv[2]
    out_file = sys.argv[3]
    offset_hours = sys.argv[4]

    customers = read_customer.read_customers(customer_file)
    customers = read_orders.read_orders(order_file, customers)

    write.print_cohort_analysis(write.generate_cohort_analysis(customers, offset_hours), out_file)

main()
