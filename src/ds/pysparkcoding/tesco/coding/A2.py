from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("A2_Round_Trips").getOrCreate()
df = spark.read.csv("../input/a2_round_trips.csv", header=True, inferSchema=True)
df_left=df.alias("left")
df_right=df.alias("right")
df.show()

(df_left.join(df_right,
    (F.col("left.destination") == F.col("right.source")) &
    (F.col("right.destination") == F.col("left.source")),
    how="inner"
).select(F.col("left.source").alias("source"), F.col("left.destination").alias("destination"))
 .filter(F.col("left.source") < F.col("left.destination")).show())

# --- Your solution below ---



# --- Verify ---
# expected = spark.read.csv("expected_output/a2_expected.csv", header=True, inferSchema=True)
# expected.show()
spark.stop()