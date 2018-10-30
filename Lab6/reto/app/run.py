from exchanges import Bitfinex
from influxdb import InfluxDBClient
from datetime import datetime
from time import sleep

# ToDo: Add tu host influx
client = InfluxDBClient('host', 8086, 'root', 'root', 'bitcoin_price')
client.create_database('bitcoin_price')

while True:
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    current_price = Bitfinex().get_current_price()
    print(current_price)
    json_body = [
        {
            "measurement": "btc_price_usd",
            "tags": {
            "provider": "bitfinex",
            },
            "time": now,
            "fields": {
                "value": float(current_price)
            }
        }
    ]
 
    client.write_points(json_body)
    sleep(5)
