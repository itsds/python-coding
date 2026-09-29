"""
================================================================================
SOLUTION — Q01: EMPLOYEES BELOW AVERAGE SALARY PER QUARTER
================================================================================
Pattern: GroupBy + Aggregation + Filter
Key Concepts: F.when/ceil for quarter derivation, multi-level aggregation, join
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q01_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Derive quarter from month
salary_with_quarter = salary.withColumn(
    "quarter",
    F.ceil(F.col("month") / 3).cast("int")
)

# Step 2: Overall average salary per (year, quarter)
overall_avg = salary_with_quarter.groupBy("year", "quarter").agg(
    F.avg("amount").alias("avg_salary")
)

# Step 3: Each employee's average salary per (year, quarter)
emp_avg = salary_with_quarter.groupBy("empid", "year", "quarter").agg(
    F.avg("amount").alias("emp_avg_salary")
)

# Step 4: Join and filter employees below the overall average
merged = emp_avg.join(overall_avg, on=["year", "quarter"])
below_avg = merged.filter(F.col("emp_avg_salary") < F.col("avg_salary"))

# Step 5: Join with employee table to get names
result = below_avg.join(employee.select("empid", "name"), on="empid") \
    .select("empid", "name", "year", "quarter", "emp_avg_salary", "avg_salary") \
    .orderBy("year", "quarter", "empid")

result.show(50, truncate=False)

# Validate
from validate import check
check(result, "q01_below_avg_quarter")

spark.stop()
