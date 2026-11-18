from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import logging

logger = logging.getLogger(__name__)

CONFIG = {
    "app_name": "A4",
    "input_path": "../input/a4_employee_salary.csv",
    "partitioned_col": "month",
    "agg_col": "salary"
}


def get_spark_session():
    spark = SparkSession.builder.appName(CONFIG["app_name"]).getOrCreate()
    return spark

def read_csv_files(spark, path):
    input_df = spark.read.csv(path,header=True,inferSchema=True)
    return input_df

def transform_data(input_df, partitioned_col, agg_col):
    window=Window.partitionBy(F.col(partitioned_col))

    transformed_df = (input_df.withColumn("max_in_month", F.max(F.col(agg_col)).over(window))
     .withColumn("min_month", F.min(F.col(agg_col)).over(window))
     .withColumn("is_highest",F.col("salary") == F.col("max_in_month"))
     .withColumn("is_lowest", F.col("salary") == F.col("min_month")))

    return transformed_df


def main():
    spark = get_spark_session()
    try:
        df = read_csv_files(spark, CONFIG["input_path"])
        transformed_df = transform_data(df,CONFIG["partitioned_col"],CONFIG["agg_col"])
        transformed_df.show(truncate=False)
    except Exception as e:
        logger.error(f"Failed Job : {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
