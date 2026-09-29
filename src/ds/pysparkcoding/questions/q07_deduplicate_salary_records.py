"""
================================================================================
Q07: DEDUPLICATE SALARY RECORDS
================================================================================
Difficulty: Medium | Pattern: Deduplication using Window + row_number

PROBLEM:
--------
The salary table may contain duplicate records for the same employee in
the same month and year. Remove duplicates by keeping only the record
with the HIGHEST salid (latest entry) for each (empid, month, year)
combination.

Return ALL columns from the salary table after deduplication.

EXPECTED OUTPUT COLUMNS:
    salid, empid, amount, month, year

SORT BY: empid, year, month

HINTS:
    - Use Window partitioned by (empid, month, year), ordered by salid DESC
    - Apply row_number() and keep only row_number == 1
    - This is the most common deduplication pattern in PySpark interviews
    - Alternative: use dropDuplicates, but window approach gives more control
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q07_DeduplicateSalaryRecords") \
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
# check(result, "q07_deduplicate_salary_records")

spark.stop()
