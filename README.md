
@'
# MQTT Learning — ProtoVolt Preparation

## Objective
Learn MQTT fundamentals, implement MQTT communication in Python, and understand how MQTT integrates with MongoDB and FastAPI.

## Learning Roadmap

### 01 — MQTT Fundamentals
- [ ] What is MQTT?
- [ ] MQTT vs HTTP
- [ ] Real-world use cases: IoT, sensors, monitoring
- [ ] Publisher, subscriber, and broker
- [ ] How a message travels

### 02 — Core MQTT Concepts
- [ ] MQTT broker vs client
- [ ] Publish and subscribe
- [ ] Topics and topic hierarchy
- [ ] Payloads: text, JSON, numbers
- [ ] Client ID
- [ ] Connect and disconnect

### 03 — Important MQTT Features
- [ ] QoS 0, 1, and 2
- [ ] Retained messages
- [ ] Last Will and Testament (LWT)
- [ ] Keep-alive and heartbeat
- [ ] Clean session and session persistence
- [ ] Wildcards: + and #

### 04 — Set Up MQTT
- [ ] Install Paho MQTT
- [ ] Choose a test broker
- [ ] Connect a Python client
- [ ] Test publishing and subscribing

### 05 — MQTT with Python
- [ ] Create publisher and subscriber scripts
- [ ] Handle connection errors
- [ ] Publish and receive messages
- [ ] Understand callback functions
- [ ] Parse JSON into Python dictionaries
- [ ] Disconnect cleanly

### 06 — Mini Project
- [ ] Simulate temperature and humidity readings
- [ ] Publish readings as JSON
- [ ] Subscribe and parse readings
- [ ] Handle multiple messages
- [ ] Test subscriber disconnection

### 07 — ProtoVolt Integration Basics
- [ ] MQTT vs REST API
- [ ] Store MQTT data in MongoDB
- [ ] Expose stored sensor data through FastAPI
- [ ] Understand the complete architecture

## Tech Stack
- Python
- Paho MQTT
- MQTT broker
- JSON
- MongoDB
- FastAPI
- Git and GitHub

## Mini Project — Sensor Monitoring

Build a Python sensor simulator that publishes temperature and humidity readings as JSON over MQTT. A subscriber receives and parses those readings.

### Architecture
Device Simulator → MQTT Broker → Subscriber → MongoDB → FastAPI

## Repository Structure

```text
mqtt-learning/
├── README.md
├── progress.md
├── MQTT_fundamentals/
├── Core_MQTT_Concepts/
├── 03_features/
├── 04_setup/
├── 05_python/
├── 06_mini_project/
└── 07_protovolt_integration/
```

## Progress Tracking
See [progress.md](progress.md) for the learning checklist and completed tasks.

## Goal
Complete the MQTT learning roadmap in one day and build a working sensor communication project.
'@ | Set-Content -Encoding utf8 README.md
