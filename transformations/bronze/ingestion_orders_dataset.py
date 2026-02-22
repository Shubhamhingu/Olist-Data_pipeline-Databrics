from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "order_id is not null",
  "rule_2": "customer_id is not null"}

@dp.create_table(name = "orders_dataset_stg")
@dp.expect_all_or_drop(rules)
def orders_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.orders_dataset")