import socket
import struct

query_codes = {
    "firmware": 0x2C,
    "application": 0x0C,
    "model": 0x46,
    "object": 0x4D,
    "object_id": 0x4B,
    "description": 0x1C,
    "location": 0x3A,
    "vendor": 0x79,
    "vendor_id": 0x78
}

def send_query(ip, port, prop_id):
    """
    Send a BACnet ReadProperty request to the target device.

    :param ip: Target device IP.
    :param port: BACnet/IP port (default 47808).
    :param prop_id: Property ID to read.
    """
    # Build the query according to the specified format
    query = struct.pack(
        ">BBHBBBBBBBIBB",  # Format as per Lua: ">BB I2 BBBBBBB I4 BB"
        0x81,  # Type: BACnet/IP (Annex J)
        0x0A,  # Function: Original-Unicast-NPDU
        0x0011,  # BVLC-Length: 17 bytes (2-byte / `H` in Python)
        # BACnet NPDU
        0x01,  # Version: ASHRAE 135-1995
        0x04,  # Control (Expecting reply)
        # BACnet APDU
        0x00,  # APDU Type: Confirmed-REQ, PDU flags: 0x0
        0x05,  # Max response segments unspecified, Max APDU size: 1476 octets
        0x01,  # Invoke ID: 1
        0x0C,  # Service Choice: readProperty
        0x0C,  # Context-specific tag, number 0, Length Value Type 4
        0x023FFFFF,  # Object Type: device; instance number 4194303 (4-byte / `I` in Python)
        0x19,  # Context-specific tag, number 1, Length Value Type 1
        prop_id  # Property ID
    )

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    try:
        # Send query to the target device
        sock.sendto(query, (ip, port))
        print(f"[+] Query sent to {ip}:{port}")

        # Receive response from the device
        response, addr = sock.recvfrom(1024)
        print(f"[+] Response from {addr}: {response.hex()}")

    except socket.timeout:
        print("[-] Timeout: No response from device")

    finally:
        # Close socket
        sock.close()

if __name__ == "__main__":
    ip_target = input("Enter Target IP: ").strip()
    send_query(ip_target, 47808, query_codes["firmware"])
    send_query(ip_target, 47808, query_codes["application"])
    send_query(ip_target, 47808, query_codes["model"])
    send_query(ip_target, 47808, query_codes["object"])
    send_query(ip_target, 47808, query_codes["object_id"])
    send_query(ip_target, 47808, query_codes["description"])
    send_query(ip_target, 47808, query_codes["location"])
    send_query(ip_target, 47808, query_codes["vendor"])
    send_query(ip_target, 47808, query_codes["vendor_id"])
