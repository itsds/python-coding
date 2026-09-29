"""
================================================================================
SOLUTION — Q02: TOP 2 EARNERS PER DEPARTMENT
================================================================================
Pattern: Window Function — dense_rank
Key Concepts: Window.partitionBy, dense_rank vs rank vs row_number
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q02_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)
department = spark.read.csv(f"{DATA_DIR}/department.csv", header=True, inferSchema=True)

# Step 1: Total 2024 salary per employee
sal_2024 = salary.filter(F.col("year") == 2024)
total_sal = sal_2024.groupBy("empid").agg(
    F.sum("amount").alias("total_salary")
)

# Step 2: Join employee → department → salary totals
emp_dept = employee.join(department, employee.department_id == department.deptid) \
    .select("empid", "name", "department_id", "dept_name")

emp_sal = emp_dept.join(total_sal, on="empid")

# Step 3: Apply dense_rank within each department
window = Window.partitionBy("department_id").orderBy(F.desc("total_salary"))

ranked = emp_sal.withColumn("rank", F.dense_rank().over(window))

# Step 4: Filter top 2
result = ranked.filter(F.col("rank") <= 2) \
    .select("empid", "name", "dept_name", "total_salary", "rank") \
    .orderBy("dept_name", "rank", "empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q02_top_earners_per_dept")

spark.stop()
