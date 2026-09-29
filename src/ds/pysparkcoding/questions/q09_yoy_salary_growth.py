"""
================================================================================
Q09: YEAR-OVER-YEAR SALARY GROWTH (Q1 2024 vs Q1 2025)
================================================================================
Difficulty: Medium-Hard | Pattern: YoY Comparison (Join + Arithmetic)

PROBLEM:
--------
Compare each employee's total Q1 salary in 2024 vs Q1 2025. Calculate
the year-over-year growth percentage.

Only include employees who have salary data in BOTH Q1 2024 and Q1 2025.

Formula: yoy_growth = ((q1_2025_total - q1_2024_total) / q1_2024_total) * 100
Round to 2 decimal places.

EXPECTED OUTPUT COLUMNS:
    empid, name, q1_2024_total, q1_2025_total, yoy_growth

SORT BY: empid

HINTS:
    - Filter salary to Q1 (months 1, 2, 3) for each year
    - Compute total per employee per year
    - Join the 2024 and 2025 totals on empid (inner join — only employees
      present in both years)
    - Compute the percentage growth
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q09_YoYSalaryGrowth") \
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
# check(result, "q09_yoy_salary_growth")

spark.stop()
