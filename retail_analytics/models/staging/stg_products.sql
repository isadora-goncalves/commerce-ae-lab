SELECT
    product_id,
    category_id,
    supplier_id,
    price
FROM {{ source('raw', 'products') }}