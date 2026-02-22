from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.create_table(name="dim_customers")
def dim_customers():
    df_customers = spark.read.table("customers_enr")
    df_geolocation = spark.read.table("geolocation_dataset_enr")
    df = df_customers.join(df_geolocation, df_customers.customer_zip_code_prefix == df_geolocation.geolocation_zip_code_prefix)
    # Select only required columns
    df = df.select(
        col("customer_id"),
        col("customer_unique_id"),
        col("customer_city"),
        col("customer_state"),
        col("customer_zip_code_prefix"),
        col("normalized_lat"),
        col("normalized_lng")
    )

    # Ensure no duplicates
    df = df.dropDuplicates(["customer_id"])

    return df