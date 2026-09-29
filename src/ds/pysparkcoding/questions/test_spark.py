from email import header

from pyspark.sql import Window
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

spark=SparkSession.builder.appName("test").master("local[*]").getOrCreate()

emp_schema=StructType([StructField("empId",IntegerType(),True),
                       StructField("name",StringType(),True),
                       StructField("dob",DateType(),True),
                       StructField("dep_id",IntegerType(),True),
                       StructField("manager_id",IntegerType(),True)])

employee_df= (spark.read.schema(emp_schema)
              .csv("D:\\repos\python-coding\src\ds\pysparkcoding\data\employee.csv", header=True))

window = Window.partitionBy("dept_id")

# employee_df2 = employee_df.withColumn("amount","r")
# employee_df.agg("")

employee_df.show(truncate=False)