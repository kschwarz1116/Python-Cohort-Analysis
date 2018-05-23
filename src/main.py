"""
This script holds the main functionality for the Cohort Analysis programming challenge.
"""

import sys
import read_customer
import read_orders
import write_analysis

def main() -> None:
    """This function accepts command line arguments and parses them into a table"""

    customer_file = "" # type: str
    order_file = "" # type: str
    if len(sys.argv) != 4:
        print("Got improper args")
        return

    customer_file = sys.argv[1]
    order_file = sys.argv[2]
    out_file = sys.argv[3]
    
    customers = read_customer.read_customers(customer_file)
    customers = read_orders.read_orders(order_file, customers)
    
    write_analysis.print_cohort_analysis(write_analysis.generate_cohort_analysis(customers), out_file)

main()
