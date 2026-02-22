from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "review_id is not null",
  "rule_2": "order_id is not null"}

@dp.create_table(name = "order_reviews_dataset_stg")
@dp.expect_all_or_drop(rules)
def order_reviews_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.order_reviews_dataset")