import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "arshiya7412/mqtt-learning/demo/temperature"


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to broker:", reason_code)
    client.subscribe(TOPIC)
    print("Subscribed to:", TOPIC)


def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")

    print(f"Received on {topic}: {payload}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="arshi_subscriber_01"
)

client.on_connect = on_connect
client.on_message = on_message
try:
    print("Connecting to broker...")
    client.connect(BROKER, PORT, 60)
    print("Connection request sent. Waiting for broker response...")
    client.loop_forever()

except KeyboardInterrupt:
    print("Subscriber stopped.")

except Exception as error:
    print("MQTT error:", error)

finally:
    client.disconnect()