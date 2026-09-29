"""
================================================================================
SOLUTION — Q11: CONDITIONAL AGGREGATION — DEPARTMENT STATS
================================================================================
Pattern: Conditional Aggregation with F.when + agg
Key Concepts: F.when inside F.sum, multi-metric aggregation, left join
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q11_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)
department = spark.read.csv(f"{DATA_DIR}/department.csv", header=True, inferSchema=True)

# Step 1: Compute each employee's average monthly salary in 2024
sal_2024 = salary.filter(F.col("year") == 2024)
emp_avg = sal_2024.groupBy("empid").agg(
    F.avg("amount").alias("avg_monthly_salary")
)

# Step 2: Join employee → department (all employees, even without salary)
emp_dept = employee.join(department, employee.department_id == department.deptid) \
    .select("empid", "name", "dept_name")

# Step 3: Left join with salary averages
emp_stats = emp_dept.join(emp_avg, on="empid", how="left")

# Step 4: Aggregate per department with conditional counting
result = emp_stats.groupBy("dept_name").agg(
    F.count("empid").alias("employee_count"),
    F.round(F.avg("avg_monthly_salary"), 2).alias("avg_salary"),
    F.round(F.max("avg_monthly_salary"), 2).alias("max_salary"),
    F.sum(
        F.when(F.col("avg_monthly_salary") > 60000, 1).otherwise(0)
    ).cast("long").alias("high_earner_count")
).orderBy("dept_name")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q11_conditional_dept_stats")

spark.stop()
