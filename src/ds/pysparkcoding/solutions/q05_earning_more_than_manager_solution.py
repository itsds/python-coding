"""
================================================================================
SOLUTION — Q05: EMPLOYEES EARNING MORE THAN THEIR MANAGER
================================================================================
Pattern: Self-Join
Key Concepts: Aliasing DataFrames, self-join, null handling
================================================================================
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Q05_Solution") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

employee = spark.read.csv(f"{DATA_DIR}/employee.csv", header=True, inferSchema=True)
salary = spark.read.csv(f"{DATA_DIR}/salary.csv", header=True, inferSchema=True)

# Step 1: Total 2024 salary per employee
sal_2024 = salary.filter(F.col("year") == 2024)
total_sal = sal_2024.groupBy("empid").agg(
    F.sum("amount").alias("total_salary")
)

# Step 2: Get employees who have managers (filter out null manager_id)
emp_with_mgr = employee.filter(F.col("manager_id").isNotNull())

# Step 3: Join employee with their salary total
emp_sal = emp_with_mgr.join(total_sal, on="empid")

# Step 4: Join manager with their salary total (self-join pattern)
mgr_sal = total_sal.withColumnRenamed("empid", "mgr_empid") \
    .withColumnRenamed("total_salary", "manager_total_salary")

emp_vs_mgr = emp_sal.join(
    mgr_sal,
    emp_sal.manager_id == mgr_sal.mgr_empid
)

# Step 5: Get manager name via another join with employee table
mgr_names = employee.select(
    F.col("empid").alias("mgr_id2"),
    F.col("name").alias("manager_name")
)

emp_vs_mgr = emp_vs_mgr.join(
    mgr_names,
    emp_vs_mgr.manager_id == mgr_names.mgr_id2
)

# Step 6: Filter where employee earns more than manager
result = emp_vs_mgr.filter(F.col("total_salary") > F.col("manager_total_salary")) \
    .select(
        "empid", "name", "total_salary",
        F.col("manager_id").cast("int").alias("manager_id"),
        "manager_name", "manager_total_salary"
    ) \
    .orderBy("empid")

result.show(truncate=False)

# Validate
from validate import check
check(result, "q05_earning_more_than_manager")

spark.stop()
