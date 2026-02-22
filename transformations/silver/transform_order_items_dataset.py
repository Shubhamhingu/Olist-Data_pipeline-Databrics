from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="order_items_dataset_enr")
def order_items_dataset_enr():
    df = spark.readStream.table("order_items_dataset_stg")
    df = df.withColumn("price", col("price").cast(DoubleType()))
    df = df.withColumn("freight_value", col("freight_value").cast(DoubleType()))
    df = df.withColumn("shipping_limit_date", col("shipping_limit_date").cast(TimestampType()))
    df = df.withColumn("shipping_date", dayofmonth(col("shipping_limit_date")))
    df = df.withColumn("shipping_month", month(col("shipping_limit_date")))
    df = df.withColumn("shipping_year", year(col("shipping_limit_date")))
    df = df.withColumn("shipping_day", dayofweek(col("shipping_limit_date")))
    df = df.withColumn("shipping_hour", hour(col("shipping_limit_date")))
    return df