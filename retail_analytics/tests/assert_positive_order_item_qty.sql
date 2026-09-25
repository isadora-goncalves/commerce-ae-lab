select *
from {{ ref('stg_order_items') }}
where qty <= 0