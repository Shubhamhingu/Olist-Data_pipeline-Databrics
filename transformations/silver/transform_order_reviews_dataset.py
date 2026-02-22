from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="orders_reviews_dataset_enr")
def orders_reviews_dataset_enr():
    df = spark.readStream.table("order_reviews_dataset_stg")
    df = df.withColumn("review_creation_date", to_date(col("review_creation_date"), "yyyy-MM-dd HH:mm:ss"))
    df = df.withColumn("review_answer_timestamp", to_date(col("review_answer_timestamp"), "yyyy-MM-dd HH:mm:ss"))
    return df