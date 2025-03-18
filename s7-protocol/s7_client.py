import sys
import snap7
from snap7.util import get_int, get_real, get_bool

COMMON_SLOTS = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (2, 1)]

def connect_plc(ip):
    client = snap7.client.Client()
    print("\n[Attempting to Connect to PLC]")

    for rack, slot in COMMON_SLOTS:
        print(f"- Trying connection to {ip} | Rack: {rack}, Slot: {slot}...")
        try:
            client.connect(ip, rack, slot)
            if client.get_connected():
                print("  > Connection successful!\n")
                return client, rack, slot
        except Exception:
            print("  > Connection failed (Connection timed out)")

    print("\n[Connection Failed]")
    return None, None, None

def get_plc_info(client):
    try:
        print("[Retrieving PLC Information]")
        order_code = client.get_order_code().OrderCode.decode("utf-8")
        cpu_info = client.get_cpu_info()
        cpu_state = client.get_cpu_state()

        print(f"- Order Code: {order_code}")
        print(f"- CPU Model: {cpu_info.ModuleTypeName.decode('utf-8')}")
        print(f"- Serial Number: {cpu_info.SerialNumber.decode('utf-8')}")
        print(f"- AS Name: {cpu_info.ASName.decode('utf-8')}")
        print(f"- Module Name: {cpu_info.ModuleName.decode('utf-8')}")
        print(f"- CPU State: {cpu_state}\n")
    except Exception as e:
        print(f"- Failed to retrieve information ({e})\n")

def scan_data_blocks(client, max_db=10):
    print("[Scanning Data Blocks (DB)]")
    available_dbs = []
    for db_number in range(1, max_db + 1):
        try:
            client.db_read(db_number, 0, 1)
            available_dbs.append(db_number)
        except Exception:
            pass
    print(f"- Found {len(available_dbs)} available DB(s).\n")
    return available_dbs

def read_data_from_dbs(client, dbs):
    print("[Reading Data Blocks Content]")
    for db in dbs:
        try:
            data = client.db_read(db, 0, 16)
            int_value = get_int(data, 0)
            real_value = get_real(data, 2)
            bool_value = get_bool(data, 4, 0)
            print(f"- DB {db}: Integer={int_value}, Float={real_value:.2f}, Boolean={'ON' if bool_value else 'OFF'}")
        except Exception as e:
            print(f"- DB {db}: Failed to read ({e})")
    print()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <PLC_IP>")
        sys.exit(1)

    plc_ip = sys.argv[1]
    client, rack, slot = connect_plc(plc_ip)

    if client:
        get_plc_info(client)
        dbs = scan_data_blocks(client)
        if dbs:
            read_data_from_dbs(client, dbs)
        client.disconnect()
        print("[Connection Closed]\n- Session complete, PLC connection closed.\n")

if __name__ == "__main__":
    main()
