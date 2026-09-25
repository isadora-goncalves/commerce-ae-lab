select *
from {{ ref('stg_promotions')}}
where discount not between 0 and 100