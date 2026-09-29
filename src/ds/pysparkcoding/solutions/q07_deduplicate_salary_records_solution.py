"""
================================================================================
SOLUTION — Q07: DEDUPLICATE SALARY RECORDS
================================================================================
Pattern: Deduplication using Window + row_number
Key Concepts: row_number vs dropDuplicates, deterministic dedup
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
    .appName("Q07_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Window approach: partition by the columns that define a "group" of
# duplicates, order by the tiebreaker (salid DESC = keep latest)
window = Window.partitionBy("empid", "month", "year").orderBy(F.desc("salid"))

deduped = salary.withColumn("rn", F.row_number().over(window)) \
    .filter(F.col("rn") == 1) \
    .drop("rn")

result = deduped.select("salid", "empid", "amount", "month", "year") \
    .orderBy("empid", "year", "month")

result.show(50, truncate=False)
print(f"Before dedup: {salary.count()} rows")
print(f"After dedup:  {result.count()} rows")

# Validate
from validate import check
check(result, "q07_deduplicate_salary_records")

spark.stop()
