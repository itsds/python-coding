"""
================================================================================
SOLUTION — Q06: EMPLOYEES WITH NO SALARY RECORDS
================================================================================
Pattern: Anti-Join (left_anti)
Key Concepts: left_anti join, finding missing/orphan records
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q06_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# The left_anti join returns rows from the LEFT table that have
# NO match in the RIGHT table. This is the cleanest PySpark way
# to find "missing" records.

result = employee.join(salary, on="empid", how="left_anti") \
    .select("empid", "name", "department_id") \
    .orderBy("empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q06_employees_with_no_salary")

spark.stop()
