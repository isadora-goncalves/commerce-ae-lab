SELECT
    store_id,
    city
FROM {{ source('raw', 'stores') }}