from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("TestPySpark") \
    .config("spark.ui.showConsoleProgress", "false") \
    .getOrCreate()

df = spark.createDataFrame(
    [(1, "Alice", 30), (2, "Bob", 25), (3, "Charlie", 35)],
    ["id", "name", "age"]
)

df.show()
spark.stop()