"""
Goals:
-Create customer class
  ID - Int
  Created - UTCTime
  [Order times] - [UTCTime]
-Import customers.csv
  Store customers in a hash table
-Import orders.csv
  Throw out orders for non-existent customers
  Update order times
-Generate output data
  Out = [[Int]]
  Out[n][m] = # of distinct orders for m weeks into the nth cohort
-Output to a csv
  
"""
