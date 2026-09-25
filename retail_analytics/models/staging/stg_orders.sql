SELECT
    order_id,
    customer_id,
    store_id,
    cast(order_date as date) as order_date,
    promotion_id
FROM {{ source ('raw', 'orders') }}