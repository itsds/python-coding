"""
================================================================================
SOLUTION — Q10: SALARY GAP DETECTION
================================================================================
Pattern: Data Quality — Cross Join + Anti-Join
Key Concepts: spark.range, crossJoin, left_anti, data completeness checks
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q10_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Create a DataFrame of all 12 months
all_months = spark.range(1, 13).withColumnRenamed("id", "month")

# Step 2: Cross join employees with all months
# This gives us every (empid, month) combination that SHOULD exist
all_emp_months = employee.select("empid", "name") \
    .crossJoin(all_months) \
    .withColumn("year", F.lit(2024))

# Step 3: Get actual salary records for 2024
actual_2024 = salary.filter(F.col("year") == 2024) \
    .select("empid", "month", "year") \
    .distinct()

# Step 4: Left anti-join to find missing months
missing = all_emp_months.join(
    actual_2024,
    on=["empid", "month", "year"],
    how="left_anti"
)

result = missing.select("empid", "name", F.col("month").alias("missing_month"), "year") \
    .orderBy("empid", "missing_month")

result.show(50, truncate=False)

# Validate
from validate import check
check(result, "q10_salary_gap_detection")

spark.stop()
