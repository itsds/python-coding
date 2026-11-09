from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions.builtin import array_join

spark = SparkSession.builder.appName("A6_String_Cleanup").getOrCreate()
df = spark.read.csv("../input/a6_string_cleanup.csv", header=True, inferSchema=True)
df.show(truncate=False)

F.initcap(F.trim(F.col("full_Name")))
# --- Your solution below ---
((df.withColumn("full_name",F.initcap(array_join(F.split(F.trim(F.col("full_name"))," ")," ",null_replacement=None)))
 .withColumn("email_domain",F.split(F.col("email"),"@")[1])
 .withColumn("phone_10digit",F.substring(F.regexp_replace(F.col("phone"),r"[\-() ]", ""),-10,10))
 .withColumn("reg_year",F.split(F.col("registration_code"),"-")[1])
 .withColumn("reg_dept",F.split(F.col("registration_code"),"-")[2])
 .withColumn("reg_seq",F.split(F.col("registration_code"),"-")[3])
 .withColumn("reg_city",F.split(F.col("registration_code"),"-")[4]))
 .drop(F.col("registration_code"),F.col("phone"),F.col("email"))
 .show(truncate=False))



# --- Verify ---
# expected = spark.read.csv("expected_output/a6_expected.csv", header=True, inferSchema=True)
# expected.show()
spark.stop()