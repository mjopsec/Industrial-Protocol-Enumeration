import sys
from pycomm3 import LogixDriver

def enumerate_plc(plc_ip):
    """Enumerate all available tags on the PLC"""
    try:
        with LogixDriver(plc_ip) as plc:
            tag_list = plc.get_tag_list()

            print(f"Tag list on {plc_ip}:")
            for tag in tag_list:
                print(f"Tag: {tag['tag_name']}, Type: {tag['data_type_name']}, Address: {tag['symbol_address']}")

            print("\nDone!")
    except Exception as e:
        print(f"An error occurred while connecting to the PLC: {e}")

def read_tag(plc_ip, tag_name):
    """Read the value of a specific tag"""
    try:
        with LogixDriver(plc_ip) as plc:
            value = plc.read(tag_name)
            print(f"Value of tag {tag_name}: {value}")
    except Exception as e:
        print(f"An error occurred while reading tag {tag_name}: {e}")

def write_tag(plc_ip, tag_name, value):
    """Write a value to a specific tag"""
    try:
        with LogixDriver(plc_ip) as plc:
            plc.write(tag_name, value)
            print(f"Successfully wrote value {value} to tag {tag_name}")
    except Exception as e:
        print(f"An error occurred while writing tag {tag_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Enumerate tags: python3 eip_client.py <PLC_IP> enum")
        print("  Read tag:       python3 eip_client.py <PLC_IP> read <TAG_NAME>")
        print("  Write tag:      python3 eip_client.py <PLC_IP> write <TAG_NAME> <VALUE>")
        sys.exit(1)

    plc_ip = sys.argv[1]
    command = sys.argv[2]

    if command == "enum":
        enumerate_plc(plc_ip)
    elif command == "read":
        if len(sys.argv) < 4:
            print("Usage: python3 eip_client.py <PLC_IP> read <TAG_NAME>")
            sys.exit(1)
        tag_name = sys.argv[3]
        read_tag(plc_ip, tag_name)
    elif command == "write":
        if len(sys.argv) < 5:
            print("Usage: python3 eip_client.py <PLC_IP> write <TAG_NAME> <VALUE>")
            sys.exit(1)
        tag_name = sys.argv[3]
        value = sys.argv[4]

        # Convert to a numeric type if possible
        try:
            if "." in value:
                value = float(value)  # Attempt to convert to float
            else:
                value = int(value)    # Attempt to convert to integer
        except ValueError:
            pass  # Remain as string if conversion fails

        write_tag(plc_ip, tag_name, value)
    else:
        print("Unrecognized command! Use enum, read, or write.")