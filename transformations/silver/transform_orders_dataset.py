from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="orders_dataset_enr")
def orders_dataset_enr():
    df = spark.readStream.table("orders_dataset_stg")
    df = df.withColumn("order_purchase_timestamp", to_timestamp(col("order_purchase_timestamp")))
    df = df.withColumn("order_approved_at", to_timestamp(col("order_approved_at")))
    df = df.withColumn("order_delivered_carrier_date", to_timestamp(col("order_delivered_carrier_date")))
    df = df.withColumn("order_delivered_customer_date", to_timestamp(col("order_delivered_customer_date")))
    df = df.withColumn("order_estimated_delivery_date", to_timestamp(col("order_estimated_delivery_date")))
    return df