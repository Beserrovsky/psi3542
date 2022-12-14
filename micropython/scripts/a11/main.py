led = machine.Pin(2, machine.Pin.OUT)
sensor = dht.DHT11(machine.Pin(15))

led_state = False
led.value(led_state)

def sub_cb(topic, msg):
  print((topic, msg))
  if (topic == topic_led_sub):
    handle_led_sub(msg)
  elif (topic == topic_term_sub):
    handle_term_sub(msg)
  elif (topic == topic_term_toggle_sub):
    handle_term_toggle_sub()
  
def handle_led_sub(msg):
  global led_state, topic_led_state_pub
  led_state = not led_state
  led.value(led_state)
  if (led_state):
    client.publish(topic_led_state_pub, b'true')
  else:
    client.publish(topic_led_state_pub, b'false')

setpoint = 22
term_state = False

def handle_term_sub(msg):
  global setpoint
  setpoint = int(msg.decode('utf8', 'strict'))
  print(str(setpoint))

def handle_term_toggle_sub():
  global term_state, topic_term_state_pub
  term_state = not term_state
  if (term_state):
    client.publish(topic_term_state_pub, b'true')
  else:
    client.publish(topic_term_state_pub, b'false')

def dht_pub():
  sensor.measure()
  temp = str(sensor.temperature())
  hum = str(sensor.humidity())
  print('DHT --> temp: %s / hum: %s' % (temp, hum))
  setpoint = temp
  client.publish(topic_temp_pub, temp)
  client.publish(topic_hum_pub, hum)

def connect_and_subscribe():
  global client_id, mqtt_server, topic_led_sub, topic_term_sub, topic_term_toggle_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_led_sub)
  client.subscribe(topic_term_sub)
  client.subscribe(topic_term_toggle_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_led_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    new_message = client.check_msg()
    if new_message != None:
      client.publish(topic_notif_pub, b'received')
    if (term_state):
      client.publish(topic_temp_pub, str(setpoint))
    else:
      dht_pub()
      # client.publish(topic_temp_pub, str(22))
    time.sleep(1)
  except OSError as e:
    restart_and_reconnect()
