SELECT
    return_id,
    order_item_id,
    refund
FROM {{ source('raw', 'returns') }}