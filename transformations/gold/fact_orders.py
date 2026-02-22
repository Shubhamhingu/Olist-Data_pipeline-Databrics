from pyspark import pipelines as dp
from pyspark.sql.functions import *

@dp.create_table(name = "fact_orders")
def fact_orders():
    df_orders = spark.read.table("orders_dataset_enr")
    df_orders_items = spark.read.table("order_items_dataset_enr")
    df_order_payments = spark.read.table("order_payments_dataset_enr")
    df = df_orders.join(df_orders_items, "order_id").join(df_order_payments, "order_id")
    df = df.select("order_id", "customer_id","order_status","order_purchase_timestamp","product_id", "seller_id", "price", "payment_value","payment_type")
    return df