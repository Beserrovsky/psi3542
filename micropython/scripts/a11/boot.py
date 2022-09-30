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
import dht


ssid = 'FamiliaOliveira - 2G'
password = 'oliveira123'
mqtt_server = '18.197.248.71'
client_id = ubinascii.hexlify(machine.unique_id())

topic_led_sub = b'led-13683702'
topic_led_state_pub = b'led_state-13683702'

topic_term_sub = b'term-13683702'
topic_term_toggle_sub = b'term_toggle-13683702'
topic_term_state_pub = b'term_state-13683702'

topic_notif_pub = b'notification-13683702'

topic_temp_pub = b'temp-13683702'
topic_hum_pub = b'hum-13683702'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
