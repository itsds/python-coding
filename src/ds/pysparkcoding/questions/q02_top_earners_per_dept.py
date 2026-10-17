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
from os import truncate

from pyspark.sql import SparkSession
import os
import sys
from pyspark.sql import functions as F, Window
from pyspark.sql.functions.builtin import dense_rank

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



result = ((employee.join(department, employee["department_id"] == department["deptid"], "inner")
           .join(salary, on="empid", how="inner")))


grouped_df = (result.groupBy(F.col("dept_name"), F.col("empid"),F.col("name"))
              .agg(F.sum("amount").alias("Total_salary")))

window_frame = Window.partitionBy("dept_name").orderBy(F.col("total_salary").desc())

final_df = grouped_df.withColumn("dense_rk", dense_rank().over(window_frame)).filter(F.col("dense_rk")<=2).select("empid", "name", "dept_name", "total_salary", F.col("dense_rk").alias("rank")).orderBy("dept_name", "dense_rk", "empid")

final_df.show(truncate=False)

# ---------- VALIDATE ----------
# Uncomment the line below when you're ready to check your answer.
# Your result DataFrame should be named 'result'.

# from validate import check
# check(result, "q02_top_earners_per_dept")

spark.stop()
