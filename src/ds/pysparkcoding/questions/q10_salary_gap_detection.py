"""
================================================================================
Q10: SALARY GAP DETECTION — FIND MISSING MONTHS
================================================================================
Difficulty: Medium-Hard | Pattern: Data Quality / Cross Join + Anti-Join

PROBLEM:
--------
For the year 2024, identify which months are MISSING for each employee.
Every employee should ideally have a salary record for all 12 months
(Jan through Dec). Find the gaps.

EXPECTED OUTPUT COLUMNS:
    empid, name, missing_month, year

SORT BY: empid, missing_month

HINTS:
    - Create a DataFrame of all 12 months: spark.range(1, 13)
    - Cross join employees with all months to get every possible combination
    - Left anti-join with actual salary records to find what's missing
    - This is a classic data-quality pattern used in production pipelines
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q10_SalaryGapDetection") \
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
# check(result, "q10_salary_gap_detection")

spark.stop()
