# MQTT Protocol Enumeration

This tool is a Python script for MQTT enumeration with data modification and filtering capabilities. The script connects to an MQTT broker, subscribes to all topics, and processes JSON messages by modifying specified values based on given filters.

## Features ✨

- :satellite: **MQTT Broker Connection:** Connects to an MQTT broker using a provided IP/hostname and port.
- :incoming_envelope: **Subscribe to All Topics:** Automatically subscribes to the `#` topic to receive all messages.
- :wrench: **Data Modification:** Modifies numeric values in JSON messages based on key=value pairs provided via the `--modify` parameter.
- :mag: **Data Filtering:** Only modifies messages that meet specific criteria defined by key=value pairs passed through the `--filter` parameter.
- :sparkles: **Formatted Output:** Displays the topic and modified message on the console in a clean, easy-to-read format.

## Prerequisites 🛠️

- Python 3.x
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)

## Installation 📥

1. Ensure you have Python 3 installed.
2. Install the `paho-mqtt` package using pip:

   ```bash
   pip install paho-mqtt
   ```

## Usage 🏃

Run the script `mqtt_client.py` with the required arguments:

```bash
python mqtt_client.py <broker> <port> [--modify key=value ...] [--filter key=value ...]
```

### Parameters

- `<broker>`: The IP address or hostname of the MQTT broker.
- `<port>`: The port number of the MQTT broker.
- `--modify`: *(Optional)* One or more key=value pairs that specify numeric values to be added to the JSON data. The value must be a number (integer or float).
- `--filter`: *(Optional)* One or more key=value pairs used to filter messages. Only messages that meet these filter criteria will be modified.

### Additional Examples

- **Read All Data:**  
  To read all messages from the broker:
  ```bash
  python mqtt_client.py 172.23.1.1 1883
  ```

- **Modify Specific Data Using Filter:**  
  To modify specific data in messages using a filter:
  ```bash
  python mqtt_client.py 172.23.1.1 1883 --modify passenger=1 --filter mac=246F2824CC44
  ```

- **Modify All Data:**  
  To modify all messages:
  ```bash
  python mqtt_client.py 172.23.1.1 1883 --modify passenger=1
  ```

> **Note:**  
> - The script listens for messages for **10 seconds** after connecting to the broker. You can adjust this duration as needed.
> - Ensure that the incoming messages are in JSON format for the modifications to work correctly.
> - If data modification fails, the original message will be displayed without changes.

## Code Structure 📂

- **on_connect:**  
  Callback executed when the connection to the broker is successful. Subscribes to all topics (`#`) if the connection is established.

- **should_modify:**  
  Checks if the JSON data meets the filter criteria.

- **modify_data:**  
  Parses the message into JSON, modifies numeric values (by addition) if they match the provided filters, and returns the modified JSON string.

- **on_message:**  
  Callback executed for each incoming message. Processes the message using `modify_data` before printing the topic and modified message.

- **enumerate_mqtt:**  
  Sets up the MQTT connection, assigns callbacks, and starts the message loop for 10 seconds.


## License 📄

This script is provided "as is" without any warranties. Use it at your own risk.