"""
This script holds the main functionality for the Cohort Analysis programming challenge.
"""

import sys

def main() -> None:
    """This function accepts command line arguments and parses them into a table"""

    customer_file = "" # type: str
    order_file = "" # type: str
    if len(sys.argv) != 3:
        print("Got improper args")
        return

    customer_file = sys.argv[1]
    order_file = sys.argv[2]

    print("Got " + customer_file + " and " + order_file)

main()
