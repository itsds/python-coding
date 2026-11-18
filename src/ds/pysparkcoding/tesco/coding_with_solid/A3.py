from pyspark.sql import SparkSession
from pyspark.sql import functions as F


CONFIG = {
    "app_name" : "A3",
    "input_path" : "../input/a3_hero_product.csv"
}

def get_spark_session():
    spark = SparkSession.builder.appName("A3").getOrCreate()
    return spark

def read_text_data(spark, path):
    text_df = spark.read.text(path)
    return text_df

def parse_df(df):
    order_products_df = (df.filter(F.col("value") != "order_data").withColumn("order_id", F.split(F.col("value"),":")[0])
     .withColumn("products", F.split(F.col("value"),":")[1]))

    order_product_df = order_products_df.withColumn("product", F.explode(F.split(F.regexp_replace(F.col("products"),"[\\[\\]]",""),",")))
    return order_product_df

def get_most_appearance_product(df):
    return df.groupBy(F.col("product")).agg(F.count("*").alias("Total_Count"))


def main():
    spark = get_spark_session()
    try:
        df = read_text_data(spark,CONFIG["input_path"])
        parsed_df = parse_df(df)
        product_df = get_most_appearance_product(parsed_df)
        product_df.show(truncate=False)
    except Exception as e:
        print(f"Failed as {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()