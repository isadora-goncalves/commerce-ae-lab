SELECT
    customer_id,
    city, 
    signup_date
FROM {{ source('raw', 'customers') }}
