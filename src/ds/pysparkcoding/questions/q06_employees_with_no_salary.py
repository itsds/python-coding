"""
================================================================================
Q06: EMPLOYEES WITH NO SALARY RECORDS
================================================================================
Difficulty: Easy | Pattern: Anti-Join (left_anti)

PROBLEM:
--------
Find all employees who have ZERO salary records in the salary table.
These are employees who exist in the employee table but have never
received any salary disbursement.

EXPECTED OUTPUT COLUMNS:
    empid, name, department_id

SORT BY: empid

HINTS:
    - Use a left_anti join: employee.join(salary, on="empid", how="left_anti")
    - Alternatively, use a left join and filter where salary columns are null
    - This pattern is very common in interviews for finding "missing" records
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q06_EmployeesWithNoSalary") \
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
# check(result, "q06_employees_with_no_salary")

spark.stop()
