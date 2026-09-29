"""
================================================================================
Q12: BROADCAST JOIN + SALARY BAND CLASSIFICATION
================================================================================
Difficulty: Medium | Pattern: Broadcast Join + F.when (CASE WHEN)

PROBLEM:
--------
Classify each employee into a salary band based on their average monthly
salary in 2024:

    < 40,000          → "Junior"
    40,000 - 60,000   → "Mid"
    60,001 - 80,000   → "Senior"
    > 80,000          → "Lead"
    No salary data    → "No Data"

Round avg_monthly_salary to 2 decimal places.

EXPECTED OUTPUT COLUMNS:
    empid, name, avg_monthly_salary, salary_band

SORT BY: empid

HINTS:
    - Compute average monthly salary per employee for 2024
    - Left join with employee table (so employees with no salary records
      still appear with null avg and "No Data" band)
    - Use F.when().when().when().otherwise() for band classification
    - In a real scenario, salary bands would come from a small lookup
      table that you'd broadcast: F.broadcast(bands_df)
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q12_BroadcastSalaryBands") \
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
# check(result, "q12_broadcast_salary_bands")

spark.stop()
