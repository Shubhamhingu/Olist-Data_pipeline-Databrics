from pyspark import pipelines as dp

# Translation Expectations
rules = {
  "rule_1": "order_id is not null",
  "rule_2": "payment_installments > 0",
  "rule_3": "payment_type in ('credit_card', 'debit_card', 'boleto', 'voucher')"}

@dp.create_table(name = "order_payments_dataset_stg")
@dp.expect_all_or_drop(rules)
def order_payments_dataset_stg():
    return spark.readStream.table("online_retail_catalog.ecommerce_schema.order_payments_dataset")