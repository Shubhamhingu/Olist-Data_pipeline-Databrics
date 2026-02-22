from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="sellers_enr")
def sellers_enr():
    df = spark.readStream.table("sellers_dataset_stg")
    df = df.withColumn('seller_city', initcap(col('seller_city')))
    return df