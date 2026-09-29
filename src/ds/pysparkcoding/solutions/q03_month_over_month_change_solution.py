"""
================================================================================
SOLUTION — Q03: MONTH-OVER-MONTH SALARY CHANGE
================================================================================
Pattern: Window Function — lag()
Key Concepts: lag, handling duplicates before windowing, null filtering
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
    .appName("Q03_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Filter to 2024 and deduplicate (keep highest salid per empid+month)
sal_2024 = salary.filter(F.col("year") == 2024)

dedup_window = Window.partitionBy("empid", "month", "year").orderBy(F.desc("salid"))
deduped = sal_2024.withColumn("rn", F.row_number().over(dedup_window)) \
    .filter(F.col("rn") == 1) \
    .drop("rn")

# Step 2: Use lag to get previous month's salary
window = Window.partitionBy("empid").orderBy("month")

with_prev = deduped.withColumn(
    "prev_amount", F.lag("amount", 1).over(window)
)

# Step 3: Compute change and filter out nulls (first month)
with_change = with_prev.withColumn(
    "salary_change", F.col("amount") - F.col("prev_amount")
).filter(F.col("prev_amount").isNotNull())

# Step 4: Join with employee for names
result = with_change.join(employee.select("empid", "name"), on="empid") \
    .select("empid", "name", "month", "year", "amount", "prev_amount", "salary_change") \
    .orderBy("empid", "month")

result.show(50, truncate=False)

# Validate
from validate import check
check(result, "q03_month_over_month_change")

spark.stop()
