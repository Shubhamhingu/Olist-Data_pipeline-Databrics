from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.create_table(name="dim_sellers")
def dim_sellers():
    df = spark.read.table("sellers_enr")

    # Select only required columns
    df = df.select(
        col("seller_id"),
        col("seller_zip_code_prefix"),
        col("seller_city"),
        col("seller_state")
    )

    # Ensure no duplicates
    df = df.dropDuplicates(["seller_id"])

    return df