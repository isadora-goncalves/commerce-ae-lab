select *
from {{ ref('stg_returns') }}
where refund <= 0