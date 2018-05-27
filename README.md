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
Customers with timestamps not in that format will be ignored.

## order_file
`orders_file` is a csv file in the following format:

1st line, headers: ignored

Subsequent lines: `order_id, order_number, user_id, created_timestamp`

`order_id` and `order_number` are ignored. `user_id` should represent the same id from `customers_file`.
`created_timestamp` should be in the format `YYYY-MM-DD HH-MM-SS`. It should represent the time the order was placed in UTC.
Orders with timestamps not in that format will be ignored.

## offset
`offset` represents a number of hours that determines the base time of the cohort groupings in ouput_file. 
E.g. -5 represents UTC-5, 3 represents UTC+3.

## output_file
`output_file` should be a path to a desired output location. It will be generated in the following format:

First, customers from `customers_file` will be grouped into cohorts based on their created time, translated to the timezone specified by offset.
Each group will span 7 days. So if the latest customer creation date was 7/30/17, the cohort bounds would be 7/24/17 - 7/30/17, 7/17/17 - 7/23/17, 7/10/17-7/17/17 etc.

Then, the output file will be generated. The ouput will be in the following format:

1st line: Cohort, Customers, 0-6 days, 7-13 days, 14-20 days, ... (as needed)
Subsequent lines: Cohort bounds, number of customers, n_0, n_1, n_2, ... (as needed)

Cohort bounds are defined above. Number of customers is the number of customers within the particular cohort.
n_m is the number of distinct customers within the given cohort that placed an order in the m-th week after their creation date.
Note that this is different from the m-th week after the beginning of the cohort bound.

# Notes
`.lint` is an executable which runs both pylint and mypy on the current code. You may need to give yourself executable permissions before running it: `chmod +x .lint`.

## Linting
I used pylint3 version 1.8.3.

## Mypy
I used mypy version 0.600. I considered using the --strict flag in `.lint`, but ran into an issue trying to type `format_tuple` in `src/write_analysis.py`

## Use of datetime
This uses the python standard library `datetime` module, in particular, its released `timezone` subclass of `tzinfo`.
`timezone` is not aware of changes in time due to things such as daylight savings or leap seconds. We could probably use something like `pytz` to remedy this, but I didn't feel that the use-case warranted it.
