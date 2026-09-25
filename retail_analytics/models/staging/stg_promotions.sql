SELECT
    promotion_id,
    discount
FROM {{ source('raw', 'promotions') }}