"""
================================================================================
Q05: EMPLOYEES EARNING MORE THAN THEIR MANAGER
================================================================================
Difficulty: Medium | Pattern: Self-Join

PROBLEM:
--------
Find employees whose TOTAL salary in 2024 is greater than their
manager's TOTAL salary in 2024. Use the manager_id column in the
employee table to identify each employee's manager.

Note: Some employees may not have a manager (manager_id is null) —
they should be excluded.

EXPECTED OUTPUT COLUMNS:
    empid, name, total_salary, manager_id, manager_name, manager_total_salary

SORT BY: empid

HINTS:
    - Compute total 2024 salary per employee
    - Self-join employee table: employee as e, employee as m where
      e.manager_id = m.empid
    - Join salary totals for both employee and manager
    - Filter where employee total > manager total
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q05_EarningMoreThanManager") \
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
# check(result, "q05_earning_more_than_manager")

spark.stop()
