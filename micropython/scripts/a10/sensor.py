import dht
from machine import Pin

sensor = dht.DHT11(Pin(15))

sensor.measure()
print(sensor.temperature())
print(sensor.humidity())
