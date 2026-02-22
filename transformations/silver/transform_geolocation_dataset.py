from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Transforming Customer Data
@dp.create_table(name="geolocation_dataset_enr")
def geolocation_dataset_enr():
    df = spark.readStream.table("geolocation_dataset_stg")
    df = df.withColumn("geolocation_zip_code_prefix", col("geolocation_zip_code_prefix").cast(IntegerType()))
    df = df.withColumn("geolocation_lat", col("geolocation_lat").cast(DoubleType()))
    df = df.withColumn("geolocation_lng", col("geolocation_lng").cast(DoubleType()))
    df = df.withColumn("geolocation_city", initcap(col("geolocation_city")))
    df = df.withColumn("normalized_lat", floor(col("geolocation_lat") * 10) / 10)
    df = df.withColumn("normalized_lng", floor(col("geolocation_lng") * 10) / 10)
    df = df.dropDuplicates(["geolocation_zip_code_prefix", "normalized_lat", "normalized_lng"])
    return df