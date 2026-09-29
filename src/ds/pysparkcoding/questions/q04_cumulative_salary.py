"""
================================================================================
Q04: CUMULATIVE (RUNNING TOTAL) SALARY PER EMPLOYEE
================================================================================
Difficulty: Medium | Pattern: Window Function — sum with rowsBetween

PROBLEM:
--------
Compute the cumulative (running total) salary for each employee across
the months of 2024. For each row, cumulative_salary should be the sum of
all salary amounts from month 1 up to and including the current month.

EXPECTED OUTPUT COLUMNS:
    empid, name, month, year, amount, cumulative_salary

SORT BY: empid, month

HINTS:
    - Filter to year 2024
    - If duplicate records exist for same (empid, month, year), keep the
      latest one (highest salid)
    - Use Window partitioned by empid, ordered by month
    - Use F.sum("amount").over(window) with rowsBetween(Window.unboundedPreceding, 0)
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q04_CumulativeSalary") \
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
# check(result, "q04_cumulative_salary")

spark.stop()
