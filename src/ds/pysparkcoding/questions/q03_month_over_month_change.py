"""
================================================================================
Q03: MONTH-OVER-MONTH SALARY CHANGE
================================================================================
Difficulty: Medium | Pattern: Window Function — lag()

PROBLEM:
--------
For each employee, calculate the month-over-month salary change in the
year 2024. Use the lag() window function to get the previous month's
salary, then compute the difference.

The first month (January) will not have a previous month — exclude those
rows from the output.

EXPECTED OUTPUT COLUMNS:
    empid, name, month, year, amount, prev_amount, salary_change

SORT BY: empid, month

HINTS:
    - Filter to year 2024
    - If duplicate records exist for same (empid, month, year), keep the
      latest one (highest salid)
    - Use Window partitioned by empid, ordered by month
    - lag("amount", 1) gives previous month's salary
    - salary_change = amount - prev_amount
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q03_MonthOverMonthChange") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)
department = spark.read.csv(f"{DATA_DIR}/department.csv", header=True, inferSchema=True)

# ---------- YOUR CODE BELOW ----------




# ---------- VALIDATE ----------
# Uncomment the line below when you're ready to check your answer.
# Your result DataFrame should be named 'result'.

# from validate import check
# check(result, "q03_month_over_month_change")

spark.stop()
