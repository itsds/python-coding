"""
================================================================================
SOLUTION — Q12: BROADCAST JOIN + SALARY BAND CLASSIFICATION
================================================================================
Pattern: Broadcast Join + F.when (CASE WHEN)
Key Concepts: F.broadcast, F.when chaining, null handling with isNull
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q12_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Compute average monthly salary per employee for 2024
sal_2024 = salary.filter(F.col("year") == 2024)
emp_avg = sal_2024.groupBy("empid").agg(
    F.round(F.avg("amount"), 2).alias("avg_monthly_salary")
)

# Step 2: Left join with employee (so employees with no salary get null)
emp_with_avg = employee.select("empid", "name").join(emp_avg, on="empid", how="left")

# Step 3: Create salary bands lookup table and broadcast it
# In practice, bands come from a config/reference table
bands = spark.createDataFrame([
    (0, 40000, "Junior"),
    (40000, 60000, "Mid"),
    (60001, 80000, "Senior"),
    (80001, 999999, "Lead"),
], ["lower", "upper", "band"])

# Step 4: Classify using F.when (the practical approach for fixed bands)
# The broadcast join approach would be:
#   emp_with_avg.join(F.broadcast(bands),
#       (emp_with_avg.avg_monthly_salary >= bands.lower) &
#       (emp_with_avg.avg_monthly_salary <= bands.upper))
# But F.when is cleaner for static ranges:

result = emp_with_avg.withColumn(
    "salary_band",
    F.when(F.col("avg_monthly_salary").isNull(), "No Data")
     .when(F.col("avg_monthly_salary") < 40000, "Junior")
     .when(F.col("avg_monthly_salary") <= 60000, "Mid")
     .when(F.col("avg_monthly_salary") <= 80000, "Senior")
     .otherwise("Lead")
).select("empid", "name", "avg_monthly_salary", "salary_band") \
 .orderBy("empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q12_broadcast_salary_bands")

spark.stop()
