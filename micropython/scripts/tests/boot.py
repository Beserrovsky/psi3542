import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'FamiliaOliveira - 2G'
password = 'oliveira123'
mqtt_server = '18.197.248.71'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'led-13683702'
topic_pub = b'notification-13683702'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
