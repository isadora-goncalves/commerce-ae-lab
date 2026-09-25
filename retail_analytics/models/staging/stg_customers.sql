SELECT
    customer_id,
    city, 
    cast (signup_date as date) as signup_date
FROM {{ source('raw', 'customers') }}
