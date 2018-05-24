"""
Creates the data model for the customer class
"""

from typing import Dict, List
import datetime as dt

class Customer:
    """A simple customer class"""

    def __init__(self, created: dt.datetime) -> None:
        """Initialize the customer"""
        self.created = created #type: dt.datetime
        self.order_times = [] #type: List[dt.datetime]

CUSTOMERS = Dict[int, Customer]
