from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "geolocation_zip_code_prefix is not null",
  "rule_2": "geolocation_city is not null",
  "rule_3": "geolocation_state is not null"}

@dp.create_table(name = "geolocation_dataset_stg")
@dp.expect_all_or_drop(rules)
def geolocation_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.geolocation_dataset")