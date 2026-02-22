from pyspark import pipelines as dp

# Seller Expectations
seller_rules = {
  "rule_1": "seller_id is not null"}

@dp.create_table(name = "sellers_dataset_stg")
@dp.expect_all_or_drop(seller_rules)
def sellers_dataset_stg():
  return spark.readStream.table("online_retail_catalog.ecommerce_schema.sellers_dataset")