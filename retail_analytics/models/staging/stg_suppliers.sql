SELECT
    supplier_id,
    country
FROM {{ source('raw', 'suppliers')}}