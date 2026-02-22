from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "customer_id is not null",
  "rule_2": "customer_zip_code_prefix is not null"}

@dp.create_table(name = "customers_dataset_stg")
@dp.expect_all_or_drop(rules)
def customers_dataset_stg():
  return spark.readStream.table("online_retail_catalog.ecommerce_schema.customers_dataset")