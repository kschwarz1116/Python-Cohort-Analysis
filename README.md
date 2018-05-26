# Python Cohort Analysis

This is a cohort analysis tool written in Python 

# Requirements
At a bare minimum, you will need python 3. I wrote this using Python 3.6.5.

# Directions
In order to run the program, from the top-level directory, run:

`python3 src/main.py <customers_file> <orders_file> <output_file> <optional=offset>`

## customers_file
`customers_file` is a csv file in the following format:

1st line, headers: ignored

Subsequent lines: `customer_id, created_timestamp`

`customer_id` should be an integer.

`created_timestamp` should be in the format `YYYY-MM-DD HH-MM-SS`. It should represent the time the customer account was created in UTC.

## order_file
`orders_file` is a csv file in the following format:

1st line, headers: ignored

Subsequent lines: `order_id, order_number, user_id, created_timestamp`

`order_id` and `order_number` are ignored. `user_id` should represent the same id from `customers_file`.
`created_timestamp` should represent the time the order was placed in UTC.

## offset
`offset` represents a number of hours that determines the base time of the cohort groupings in ouput_file. 
E.g. -5 represents UTC-5, 3 represents UTC+3.

## output_file
`output_file` will be generated in the following format:

First, customers from `customers_file` will be grouped based on their created time, translated to the timezone specified by offset.
Each group will span 7 days. So if the latest customer creation date was 7/30/17, the cohort bounds would be 7/24/17 - 7/30/17, 7/17/17 - 7/23/17, 7/10/17-7/17/17 etc.


# Layout

# Notes
