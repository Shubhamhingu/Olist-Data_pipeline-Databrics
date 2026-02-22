from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="products_dataset_enr")
def products_dataset_enr():
    df = spark.readStream.table("products_dataset_stg")
    return df