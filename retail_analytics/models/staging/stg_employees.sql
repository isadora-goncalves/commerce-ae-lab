SELECT
    employee_id,
    store_id,
    salary
FROM {{ source('raw', 'employees') }}