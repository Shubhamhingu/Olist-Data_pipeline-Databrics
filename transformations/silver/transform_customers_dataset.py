from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="customers_enr")
def customers_enr():
    df = spark.readStream.table("customers_dataset_stg")
    df = df.withColumn('customer_city', initcap(col('customer_city')))
    df = df.withColumn('customer_zip_code_prefix', col('customer_zip_code_prefix').cast(IntegerType()))
    df = df.dropDuplicates(["customer_id"])
    return df