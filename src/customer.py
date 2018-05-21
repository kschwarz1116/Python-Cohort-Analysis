"""
Creates the data model for the customer class
"""

from typing import List
import datetime

class Customer:
    """A simple customer class"""

    def __init__(self, created: datetime.datetime) -> None:
        """Initialize the customer"""
        self.created = created #type: datetime.datetime
        self.order_times = [] #type: List[datetime.datetime]
