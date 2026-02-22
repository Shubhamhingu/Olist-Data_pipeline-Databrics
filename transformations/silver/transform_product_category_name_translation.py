from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="product_category_name_translation_enr")
def product_category_name_translation_enr():
    df = spark.readStream.table("product_category_name_translation_stg")
    df = df.withColumn("product_category_name_english", initcap(col("product_category_name_english")))
    return df