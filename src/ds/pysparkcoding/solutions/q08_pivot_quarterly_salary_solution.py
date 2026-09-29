"""
================================================================================
SOLUTION — Q08: PIVOT — QUARTERLY TOTAL SALARY
================================================================================
Pattern: Pivot / Reshape
Key Concepts: .pivot(), column renaming, groupBy + pivot + agg
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q08_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Filter to 2024 and derive quarter
sal_2024 = salary.filter(F.col("year") == 2024) \
    .withColumn("quarter", F.ceil(F.col("month") / 3).cast("int"))

# Step 2: Pivot — total salary per employee per quarter
pivoted = sal_2024.groupBy("empid") \
    .pivot("quarter", [1, 2, 3, 4]) \
    .agg(F.sum("amount"))

# Step 3: Rename pivoted columns (1 → Q1, 2 → Q2, etc.)
pivoted = pivoted \
    .withColumnRenamed("1", "Q1") \
    .withColumnRenamed("2", "Q2") \
    .withColumnRenamed("3", "Q3") \
    .withColumnRenamed("4", "Q4")

# Step 4: Join with employee for names
result = pivoted.join(employee.select("empid", "name"), on="empid") \
    .select("empid", "name", "Q1", "Q2", "Q3", "Q4") \
    .orderBy("empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q08_pivot_quarterly_salary")

spark.stop()
