from pyspark.sql import SparkSession
from pyspark.sql import functions as F

CONFIG = {
    "app_name" : "A2",
    "path" : "../input/a2_round_trips.csv",
    "source_col" : "source",
    "destination_col" : "destination"
}

def get_session():
    spark = SparkSession.builder.appName(CONFIG["app_name"]).getOrCreate()
    return spark

def read_csv(spark, path):
    df = spark.read.csv(path,header=True,inferSchema=True)
    return df

def transform_df(df, source_col, destination_col):
    df_left = df.alias("left")
    df_right = df.alias("right")

    df_joined=((df_left.join(df_right,
                  (F.col(f"left.{source_col}") == F.col(f"right.{destination_col}")) &
                  (F.col(f"right.{source_col}") == F.col(f"left.{destination_col}")),
                  how="inner")).
               select(F.col(f"left.{source_col}"), F.col(f"left.{destination_col}"))
               .filter(F.col(f"left.{source_col}") < F.col(f"left.{destination_col}")))

    return df_joined

def main():
    spark = get_session()
    try:
        df = read_csv(spark,CONFIG["path"])
        df.show(truncate=False)
        transformed_df = transform_df(df,CONFIG["source_col"],CONFIG["destination_col"])
        transformed_df.show(truncate=False)
    except Exception as e:
        print(f" Job Failed {e}")
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()