"""
================================================================================
Q01: EMPLOYEES BELOW AVERAGE SALARY PER QUARTER
================================================================================
Difficulty: Easy-Medium | Pattern: GroupBy + Aggregation + Filter

PROBLEM:
--------
Identify employees whose AVERAGE salary in a given quarter is LESS than
the overall average salary for that quarter (across all employees).

Quarters: Q1 = Jan-Mar, Q2 = Apr-Jun, Q3 = Jul-Sep, Q4 = Oct-Dec

EXPECTED OUTPUT COLUMNS:
    empid, name, year, quarter, emp_avg_salary, avg_salary

SORT BY: year, quarter, empid

HINTS:
    - Derive quarter from the month column
    - First compute the overall average salary per (year, quarter)
    - Then compute each employee's average salary per (year, quarter)
    - Join and filter
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q01_BelowAvgQuarter") \
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
# check(result, "q01_below_avg_quarter")

spark.stop()
