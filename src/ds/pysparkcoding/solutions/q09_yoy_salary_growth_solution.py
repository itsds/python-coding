"""
================================================================================
SOLUTION — Q09: YEAR-OVER-YEAR SALARY GROWTH
================================================================================
Pattern: YoY Comparison (Join + Arithmetic)
Key Concepts: Filtering by year, self-join on empid, percentage calc
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q09_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Filter to Q1 (months 1-3) across both years
q1_data = salary.filter(
    (F.col("month") >= 1) & (F.col("month") <= 3)
)

# Step 2: Total Q1 salary per employee per year
q1_totals = q1_data.groupBy("empid", "year").agg(
    F.sum("amount").alias("q1_total")
)

# Step 3: Split into 2024 and 2025
q1_2024 = q1_totals.filter(F.col("year") == 2024) \
    .select("empid", F.col("q1_total").alias("q1_2024_total"))

q1_2025 = q1_totals.filter(F.col("year") == 2025) \
    .select("empid", F.col("q1_total").alias("q1_2025_total"))

# Step 4: Inner join — only employees present in both years
yoy = q1_2024.join(q1_2025, on="empid")

# Step 5: Calculate YoY growth percentage
yoy = yoy.withColumn(
    "yoy_growth",
    F.round(
        (F.col("q1_2025_total") - F.col("q1_2024_total"))
        / F.col("q1_2024_total") * 100,
        2
    )
)

# Step 6: Join with employee for names
result = yoy.join(employee.select("empid", "name"), on="empid") \
    .select("empid", "name", "q1_2024_total", "q1_2025_total", "yoy_growth") \
    .orderBy("empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q09_yoy_salary_growth")

spark.stop()
