from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions.builtin import explode

spark = SparkSession.builder.appName("A7_Store_Products").getOrCreate()
# NOTE: Variable-length data — use spark.read.text(), NOT csv
df = spark.read.text("../input/a7_store_products.txt")
df.show(truncate=False)

df2=(df.withColumn("store",F.split(F.col("value"),",")[0])
 .withColumn("product", F.slice(F.split(F.col("value"),","),2,F.size(F.split(F.col("value"),","))))).drop("value")

df3=df2.withColumn("products", explode(F.col("product"))).drop(F.col("product"))

df3.filter(F.col("products") == "P1").show()
df3.groupBy(F.col("products")).agg(F.count("*").alias("store_count")).show(truncate=False)

# --- Your solution below ---



# --- Verify ---
# expected = spark.read.csv("expected_output/a7_expected.csv", header=True, inferSchema=True)
# expected.show()
spark.stop()