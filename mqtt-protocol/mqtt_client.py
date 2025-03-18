import paho.mqtt.client as mqtt
import time
import argparse
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[+] Connected to MQTT broker")
        client.subscribe("#")
    else:
        print("[-] Connection failed with code", rc)

def should_modify(data, filters):
    """Check if the data matches the given filters."""
    for key, value in filters.items():
        if key in data and str(data[key]) != value:
            return False
    return True

def modify_data(message, modifications, filters):
    try:
        data = json.loads(message)
        if should_modify(data, filters):
            for key, value in modifications.items():
                if key in data:
                    if isinstance(data[key], (int, float)):
                        data[key] += value
                    elif isinstance(data[key], str) and data[key].replace('.', '', 1).isdigit():
                        data[key] = str(float(data[key]) + value)
        return json.dumps(data)
    except Exception as e:
        print("[-] Failed to modify data:", str(e))
        return message

def on_message(client, userdata, msg):
    modifications, filters = userdata
    modified_message = modify_data(msg.payload.decode('utf-8', 'ignore'), modifications, filters)
    print(f"[+] Topic: {msg.topic}, Modified Message: {modified_message}")

def enumerate_mqtt(broker, port, modifications, filters):
    client = mqtt.Client(userdata=(modifications, filters))
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        print("[*] Connecting to broker...")
        client.connect(broker, port, 60)
        client.loop_start()
        time.sleep(10)  # Biarkan client mendengarkan pesan selama beberapa detik
        client.loop_stop()
    except Exception as e:
        print("[-] Failed to connect:", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MQTT Enumeration Tool with Data Modification and Filtering")
    parser.add_argument("broker", help="MQTT broker IP or hostname")
    parser.add_argument("port", type=int, help="MQTT broker port")
    parser.add_argument("--modify", nargs='*', help="Modify key=value pairs in received data")
    parser.add_argument("--filter", nargs='*', help="Filter key=value pairs to selectively modify data")

    args = parser.parse_args()
    modifications = {}
    filters = {}

    if args.modify:
        for mod in args.modify:
            key, value = mod.split('=')
            try:
                modifications[key] = float(value)
            except ValueError:
                print(f"[-] Invalid modification value for {key}: {value}")

    if args.filter:
        for flt in args.filter:
            key, value = flt.split('=')
            filters[key] = value

    enumerate_mqtt(args.broker, args.port, modifications, filters)