from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions.builtin import substring
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("A1_Substring_Sales").getOrCreate()

df = spark.read.csv("../input/a1_substring_sales.csv", header=True, inferSchema=True)

window_5char = Window.partitionBy(substring(F.col("subgroup"), 1, 5))
window_4char = Window.partitionBy(substring(F.col("subgroup"), 1, 4))
window_3char = Window.partitionBy(substring(F.col("subgroup"), 1, 3))

df.show()
result_df = (df.withColumn("sales_5char", F.sum("sales").over(window_5char))
 .withColumn("sales_4char",F.sum("sales").over(window_4char))
 .withColumn("sales_3char",F.sum("sales").over(window_3char)))

result_df.show()

# --- Your solution below ---

# --- Verify ---
expected = spark.read.csv("../input/a1_expected.csv", header=True, inferSchema=True)
expected.show()

spark.stop()