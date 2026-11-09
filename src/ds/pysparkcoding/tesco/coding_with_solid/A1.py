from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions.builtin import window
from pyspark.sql.window import Window

CONFIG = {
    "app_name": "A1_Substring_Sales",
    "input_path": "../input/a1_substring_sales.csv",
    "char_lengths": [5, 4, 3],
    "subgroup_col": "subgroup",
    "sales_col": "sales"
}

def get_session():
    spark = SparkSession.builder.appName(CONFIG["app_name"]).getOrCreate()
    return spark

def read_csv(spark, path):
    input_df = spark.read.csv(path,header=True,inferSchema=True)
    return input_df

def transform_df(df, nums,subgroup, sales):

    for n in nums:
        window = Window.partitionBy(F.substring(F.col(subgroup),1,n))
        column_nm = f"sales_{n}char"
        df = df.withColumn(column_nm,F.sum(F.col(sales)).over(window))

    return df

def show_df(transformed_df):
    transformed_df.show(truncate=False)

def main():
    input_path = CONFIG["input_path"]
    nums = CONFIG["char_lengths"]
    spark = get_session()
    try:
        input_df = read_csv(spark,input_path)
        show_df(input_df)
        transformed_df = transform_df(input_df,nums,CONFIG["subgroup_col"],CONFIG["sales_col"])
        show_df(transformed_df)
    except Exception as e:
        print(f"Job failed : {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()

# First Feedback
# 1. Remove unused Imports
# 2. No Config Dictionary
# 3. Transform_df not parameterized
# 4. No Exception Handling
# 5. Variable naming — input_df carried through transform
# 6. Spark.stop