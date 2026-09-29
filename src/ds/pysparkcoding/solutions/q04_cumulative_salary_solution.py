"""
================================================================================
SOLUTION — Q04: CUMULATIVE (RUNNING TOTAL) SALARY
================================================================================
Pattern: Window Function — sum with rowsBetween
Key Concepts: Running totals, unboundedPreceding, frame specification
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
    .appName("Q04_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Filter to 2024 and deduplicate
sal_2024 = salary.filter(F.col("year") == 2024)

dedup_window = Window.partitionBy("empid", "month", "year").orderBy(F.desc("salid"))
deduped = sal_2024.withColumn("rn", F.row_number().over(dedup_window)) \
    .filter(F.col("rn") == 1) \
    .drop("rn")

# Step 2: Define cumulative window
cum_window = Window.partitionBy("empid") \
    .orderBy("month") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Step 3: Compute cumulative salary
with_cumulative = deduped.withColumn(
    "cumulative_salary", F.sum("amount").over(cum_window)
)

# Step 4: Join with employee for names
result = with_cumulative.join(employee.select("empid", "name"), on="empid") \
    .select("empid", "name", "month", "year", "amount", "cumulative_salary") \
    .orderBy("empid", "month")

result.show(50, truncate=False)

# Validate
from validate import check
check(result, "q04_cumulative_salary")

spark.stop()
