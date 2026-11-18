from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import logging

logger = logging.getLogger(__name__)

CONFIG = {
    "input_path" : "../input/a6_string_cleanup.csv",
    "app_name" : "A6",
}

def get_spark_session():
    return SparkSession.builder.appName(CONFIG["app_name"]).getOrCreate()

def read_csv_data(spark, path):
    input_df = spark.read.csv(path,header=True,inferSchema=True)
    if input_df.limit(1).count() == 0:
        logger.error("Empty DataFrame")
        return None
    return input_df

def clean_name(input_df):
    return (input_df
            .withColumn("clean_name", F.initcap(F.regexp_replace(F.col("full_name"),"[ ]+"," "))).drop(F.col("full_name")))

def get_domain(input_df):
    return (input_df
            .withColumn("email_domain",F.split(F.col("email"),"@")[1]).drop(F.col("email")))

def clean_phone_num(input_df):
    return (input_df
            .withColumn("phone_10digit",F.substring(F.regexp_replace(F.col("phone"),"[^0-9]",""),-10,10)).drop(F.col("phone")))

def transform_registration(input_df):
    return (input_df
     .withColumn("reg_year",F.split(F.col("registration_code"),"-")[1])
     .withColumn("reg_dept",F.split(F.col("registration_code"),"-")[2])
     .withColumn("reg_seq",F.split(F.col("registration_code"),"-")[3])
     .withColumn("reg_city",F.split(F.col("registration_code"),"-")[4])).drop(F.col("registration_code"))


def main():
    spark = get_spark_session()
    try:
        input_data = read_csv_data(spark,CONFIG["input_path"])
        transformed_df = (input_data
                      .transform(clean_name)
                      .transform(get_domain)
                      .transform(clean_phone_num)
                      .transform(transform_registration))
        transformed_df.show()
    except Exception as e:
        logger.error("Failed Job {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()