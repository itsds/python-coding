from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions.builtin import explode

from src.ds.pysparkcoding.questions.q01_below_avg_quarter import final_df

spark = SparkSession.builder.appName("A3_Hero_Product").getOrCreate()

df = spark.read.text("../input/a3_hero_product.csv")

df.show(truncate=False)
extracted_df = (df.filter(F.col("value") != 'order_data')
                .withColumn("order_id",F.split(F.col("value"),":")[0])
                .withColumn("product", F.split(F.col('value'),':')[1])
                .drop(F.col("value")))
extracted_df.show(truncate=False)

final_df=extracted_df.select(F.col("order_id"), explode(F.split(F.regexp_replace(F.col("product"),"[\\[\\]]",""),",")).alias("products"))
final_df.groupBy(F.col("products")).agg(F.count("*").alias("Total_order")).show()


# --- Your solution below ---

# --- Verify ---
# expected = spark.read.csv("expected_output/a3_expected.csv", header=True, inferSchema=True)
# expected.show()

spark.stop()