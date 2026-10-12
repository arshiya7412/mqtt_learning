import json
payload = '{"sensor_id": "Sensor-01", "temperature": 28.5, "location": "Lab-A"}'
data = json.loads(payload)
print(data["temperature"])
print(data["location"])