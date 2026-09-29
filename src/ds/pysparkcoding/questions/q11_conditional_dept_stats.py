"""
================================================================================
Q11: CONDITIONAL AGGREGATION — DEPARTMENT-LEVEL STATS
================================================================================
Difficulty: Medium | Pattern: Conditional Aggregation with F.when + agg

PROBLEM:
--------
For each department, compute the following statistics based on 2024 data:

1. employee_count  — total number of employees in the department
                     (including those with no salary records)
2. avg_salary      — average of each employee's average monthly salary
                     (round to 2 decimal places)
3. max_salary      — highest average monthly salary in the department
                     (round to 2 decimal places)
4. high_earner_count — number of employees whose average monthly salary
                       is GREATER than 60,000

EXPECTED OUTPUT COLUMNS:
    dept_name, employee_count, avg_salary, max_salary, high_earner_count

SORT BY: dept_name

HINTS:
    - First compute each employee's average monthly salary in 2024
    - Join employees with departments (left join so employees without
      salary data are counted in employee_count)
    - Use F.when(condition, 1) inside F.sum() or F.count() for
      conditional aggregation
    - Group by department
================================================================================
"""
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- BOILERPLATE (DO NOT MODIFY) ----------
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q11_ConditionalDeptStats") \
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
# check(result, "q11_conditional_dept_stats")

spark.stop()
