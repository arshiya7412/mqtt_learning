import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "arshiya7412/mqtt-learning/demo/temperature"

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="arshi_publisher_01"
)

client.connect(BROKER, PORT, 60)
client.loop_start()

message = "28"

info = client.publish(TOPIC, message, qos=1)
info.wait_for_publish()

print("Published:", message)

client.disconnect()
client.loop_stop()