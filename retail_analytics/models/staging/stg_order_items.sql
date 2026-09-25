SELECT
    order_item_id,
    order_id,
    product_id,
    cast(qty as integer) as qty,
    cast(price as decimal(12, 2)) as price
FROM {{source('raw', 'order_items')}}