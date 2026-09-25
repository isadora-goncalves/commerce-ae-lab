SELECT
    order_id,
    customer_id,
    store_id,
    order_date,
    promotion_id
FROM {{ source ('raw', 'orders') }}