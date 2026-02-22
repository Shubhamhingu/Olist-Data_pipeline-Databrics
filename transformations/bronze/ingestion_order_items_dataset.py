from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "order_id is not null",
  "rule_2": "product_id is not null",
  "rule_3": "seller_id is not null"}

@dp.create_table(name = "order_items_dataset_stg")
@dp.expect_all_or_drop(rules)
def order_items_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.order_items_dataset")