# webapp2024


## Endpoint de tarificación de uso de servicios

POST /consumo/<servicio>

BODY
```json
{
    'id': '123',
    'unit' : 'min',
    'quantity' : 122,
    'id_tariff': 'HIGH_1'
}
```
