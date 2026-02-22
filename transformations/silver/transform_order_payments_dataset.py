from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="order_payments_dataset_enr")
def order_payments_dataset_enr():
    df = spark.readStream.table("order_payments_dataset_stg")
    df = df.withColumn("payment_value", col("payment_value").cast(DoubleType()))
    df = df.withColumn("payment_installments", col("payment_installments").cast(IntegerType()))
    return df