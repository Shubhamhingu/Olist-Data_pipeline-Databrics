from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "product_category_name is not null",
  "rule_2": "product_category_name_english is not null"}

@dp.create_table(name = "product_category_name_translation_stg")
@dp.expect_all_or_drop(rules)
def product_category_name_translation_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.product_category_name_translation")