"""
================================================================================
Q08: PIVOT — QUARTERLY TOTAL SALARY
================================================================================
Difficulty: Medium | Pattern: Pivot / Reshape

PROBLEM:
--------
Create a pivoted view of each employee's total salary per quarter in
2024. The output should have one row per employee with separate columns
for Q1, Q2, Q3, and Q4 totals.

EXPECTED OUTPUT COLUMNS:
    empid, name, Q1, Q2, Q3, Q4

SORT BY: empid

HINTS:
    - First derive the quarter from the month column
    - Compute total salary per (empid, quarter)
    - Use .groupBy("empid").pivot("quarter").sum("amount")
    - Rename pivoted columns to Q1, Q2, Q3, Q4
    - Join with employee table to get names
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q08_PivotQuarterlySalary") \
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
# check(result, "q08_pivot_quarterly_salary")

spark.stop()
