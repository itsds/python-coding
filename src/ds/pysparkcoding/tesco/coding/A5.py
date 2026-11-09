from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("A5_Access_Log").getOrCreate()
df = spark.read.csv("../input/a5_access_log.csv", header=True, inferSchema=True)
df.show()

# --- Your solution below ---
df.select(F.countDistinct("ip_address")).show()

df.groupBy(F.col("endpoint")).agg(F.count("*").alias("request_count")).show()

df.groupBy(F.col("endpoint")).agg(F.countDistinct(F.col("ip_address")).alias("unique_ip_count")).show()




# --- Verify ---
# expected = spark.read.csv("expected_output/a5_expected.csv", header=True, inferSchema=True)
# expected.show()
spark.stop()