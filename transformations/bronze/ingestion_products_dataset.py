from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "product_id is not null",
  "rule_2": "product_category_name is not null"}

@dp.create_table(name = "products_dataset_stg")
@dp.expect_all_or_drop(rules)
def products_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.products_dataset")