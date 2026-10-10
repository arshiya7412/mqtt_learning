# Module 02 --- Core MQTT Concepts

## 1. MQTT Broker vs MQTT Client

-   **Broker:** A service that receives MQTT messages and forwards them
    to subscribers whose subscriptions match.
-   **Client:** A device or program that connects to a broker to publish
    messages, subscribe to messages, or both.
-   MQTT is the communication protocol; the broker is the service that
    handles message routing.

Example: - A temperature sensor is an MQTT client. - A monitoring
dashboard is another MQTT client. - The broker routes messages between
them.

## 2. Publish and Subscribe

-   **Publish:** Send a message to the broker under a topic.
-   **Subscribe:** Tell the broker which topic or topics you want to
    receive messages from.

Example: - A sensor publishes `28` to `factory/room1/temperature`. - A
dashboard subscribes to `factory/room1/temperature`.

A subscriber normally needs to subscribe before a live message is
published to receive that message. Retained messages are a special case
covered in Module 03.

## 3. Topics and Topic Hierarchy

A **topic** is a text name used to organize MQTT messages. The `/`
character separates topic levels.

Examples:

-   `factory/room1/temperature`
-   `factory/room1/humidity`
-   `factory/room2/temperature`

In `factory/room1/temperature`: - `factory` identifies the system or
location. - `room1` identifies the room. - `temperature` identifies the
measurement.

Topics are case-sensitive: `Temperature` and `temperature` are
different. A topic is a name, not necessarily a real folder or file.

## 4. Payloads

The **payload** is the actual content carried by an MQTT message.

Examples:

Plain text: `Machine is running`

Number: `28`

JSON:

``` json
{"temperature": 28, "humidity": 65}
```

MQTT transports the payload; it does not automatically turn JSON into a
Python dictionary. In Python, the received payload is commonly bytes.
Decode it and use `json.loads()` to parse a JSON string into a Python
dictionary.

## 5. Client ID

A **client ID** identifies a client connection to the broker.

Examples: - `temperature_sensor_01` - `factory_dashboard`

Client IDs should be unique among clients connected to the same broker
at the same time. If two clients use the same ID, the broker may
disconnect the earlier connection.

## 6. Connect and Disconnect

A typical client workflow is:

1.  Connect to the broker.
2.  Subscribe to topics if messages need to be received.
3.  Publish messages if data needs to be sent.
4.  Disconnect cleanly when finished.

We will implement this workflow using Python and `paho-mqtt` in later
modules.

## Quick Revision

-   **Broker:** Receives and routes messages.
-   **Client:** A device or program connected to the broker.
-   **Publish:** Send a message.
-   **Subscribe:** Register interest in messages on a topic.
-   **Topic:** The name used to route and organize messages.
-   **Payload:** The actual message content.
-   **Client ID:** The identifier used for the client's connection.
