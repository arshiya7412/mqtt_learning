import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "factory/room1/temperature"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

print("Broker:", BROKER)
print("Port:", PORT)
print("MQTT Created successfully")

try:
  client.connect(BROKER, PORT, 60)
  client.loop_start()
  print("loop started successfully")

  message = 28
  client.publish(TOPIC, message)
  print("Publish", message)

except OSError as error:
  print("Connection failed", error)
  
finally:
  client.disconnect()
  client.loop_stop()
  print("client disconnected")