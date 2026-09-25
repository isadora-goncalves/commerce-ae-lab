SELECT
    shipment_id,
    order_id,
    status
FROM {{source('raw', 'shipments')}}