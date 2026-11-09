from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("A4_Employee_Salary").getOrCreate()
df = spark.read.csv("../input/a4_employee_salary.csv", header=True, inferSchema=True)
df.show()

# --- Your solution below ---

window = Window.partitionBy("month")

((df.withColumn("Max_in_month", F.max(F.col("salary")).over(window))
 .withColumn("min_in_month", F.min(F.col("salary")).over(window)))
 .withColumn("is_highest", F.col("salary") == F.col("Max_in_month"))
 .withColumn("is_lowest", F.col("salary") == F.col("min_in_month"))
 .show(truncate=False))


# --- Verify ---
# expected = spark.read.csv("expected_output/a4_expected.csv", header=True, inferSchema=True)
# expected.show()
spark.stop()