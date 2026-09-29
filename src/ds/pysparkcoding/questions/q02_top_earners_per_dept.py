"""
================================================================================
Q02: TOP 2 EARNERS PER DEPARTMENT
================================================================================
Difficulty: Medium | Pattern: Window Function — dense_rank

PROBLEM:
--------
Find the top 2 highest-paid employees in each department based on their
TOTAL salary in the year 2024. Use dense_rank() so that employees with
the same total salary get the same rank.

EXPECTED OUTPUT COLUMNS:
    empid, name, dept_name, total_salary, rank

SORT BY: dept_name, rank, empid

HINTS:
    - Filter salary data to year 2024
    - Compute total salary per employee
    - Join with employee and department tables
    - Use Window + dense_rank() partitioned by department
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q02_TopEarnersPerDept") \
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
# check(result, "q02_top_earners_per_dept")

spark.stop()
