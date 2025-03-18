# BACnet Protocol Enumeration

This tool is a simple BACnet/IP client that sends ReadProperty requests to a target device using UDP. It queries various BACnet properties (such as firmware, application, model, etc.) from the target device and prints the hexadecimal response.

## Features

- **BACnet ReadProperty Requests:** Sends BACnet/IP queries to read device properties.
- **Multiple Property Queries:** Automatically queries for firmware, application, model, object, object ID, description, location, vendor, and vendor ID.
- **Simple UDP Communication:** Uses Python's `socket` module to send and receive UDP packets.
- **Quick Setup:** Designed for fast testing and evaluation of BACnet/IP devices.

## Prerequisites

- Python 3.x  
  (Tested with Python 3.6+)

No external libraries are required beyond Python's standard library.

## Usage

1. **Clone or Download the Repository**

   Ensure that you have the `bacnet_client.py` script in your working directory.

2. **Run the Script**

   Execute the script using Python:

   ```bash
   python bacnet_client.py
   ```

3. **Provide the Target IP**

   When prompted, enter the target device's IP address:

   ```
   Enter Target IP:
   ```

   The tool will then send BACnet ReadProperty requests to the default BACnet/IP port (47808) for several properties and print the responses.

## How It Works

- The script builds a BACnet ReadProperty request using Python's `struct` module with a fixed header and payload.
- It sends the query using a UDP socket to the specified target IP and port.
- After sending the query, it waits for a response. If a response is received within the timeout period, the response is printed in hexadecimal format; otherwise, a timeout message is displayed.

## Example

After running the script, you might see output similar to the following:

```
Enter Target IP: 192.168.1.100
[+] Query sent to 192.168.1.100:47808
[+] Response from ('192.168.1.100', 47808): 810a0011...
```

This indicates that the query was successfully sent and a response was received from the device.

## License

This tool is provided "as is" without any warranties. Use it at your own risk.