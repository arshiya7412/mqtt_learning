
import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "factory/room1/temperature"

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected:", reason_code)
    client.subscribe(TOPIC)

def on_message(client, userdata, message):
    print(message.payload.decode("utf-8"))

client.on_message = on_message
client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_forever()