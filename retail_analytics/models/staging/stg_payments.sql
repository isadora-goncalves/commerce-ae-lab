SELECT
    payment_id,
    order_id,
    amount
FROM {{ source('raw', 'payments') }}