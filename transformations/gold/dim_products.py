from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.create_table(name="dim_products")
def dim_products():
    df = spark.read.table("products_dataset_enr")
    df2 = spark.read.table("product_category_name_translation_enr")
    joinedDf = df.join(df2, df.product_category_name == df2.product_category_name, "left")
    df = joinedDf.select(
        col("product_id"), 
        col("product_category_name_english"), 
        col("products_dataset_enr.product_category_name"), 
        col("product_name_lenght"), 
        col("product_description_lenght"), 
        col("product_photos_qty"), 
        col("product_weight_g"), 
        col("product_length_cm"), 
        col("product_height_cm"), 
        col("product_width_cm")
    )

    # Ensure no duplicates
    df = df.dropDuplicates(["product_id"])

    return df