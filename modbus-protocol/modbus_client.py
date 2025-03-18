import argparse
from pymodbus.client import ModbusTcpClient

def read_coil(ip, port, address, count):
    try:
        client = ModbusTcpClient(ip, port=int(port))
        client.connect()
        response = client.read_coils(int(address), count=int(count))
        client.close()
        if response.isError():
            print("Error:", response)
        else:
            for index, value in enumerate(response.bits):
                print(f"Coil {int(address) + index}: {value}")
    except Exception as e:
        print("Error:", e)

def write_coil(ip, port, address, value):
    try:
        client = ModbusTcpClient(ip, port=int(port))
        client.connect()
        response = client.write_coil(int(address), bool(int(value)))
        client.close()
        if response.isError():
            print("Error", response)
        else:
            print(f"Coil {value} write successful to address {address}")
    except Exception as e:
        print("Error:", e)

def read_register(ip, port, address, count):
    try:
        client = ModbusTcpClient(ip, port=int(port))
        client.connect()
        response = client.read_holding_registers(int(address), count=int(count))
        client.close()
        if response.isError():
            print("Error:", response)
        else:
            for index, value in enumerate(response.registers):
                print(f"Register {int(address) + index}: {value}")
    except Exception as e:
        print("Error:", e)

def write_register(ip, port, address, value):
    try:
        client = ModbusTcpClient(ip, port=int(port))
        client.connect()
        response = client.write_register(int(address), int(value))
        client.close()
        if response.isError():
            print("Error:", response)
        else:
            print(f"Register {value} write successful to address {address}")
    except Exception as e:
        print("Error:", e)

def main():
    parser = argparse.ArgumentParser(description="Modbus TCP CLI Tool")
    parser.add_argument("command", choices=["read_coil", "write_coil", "read_register", "write_register"])
    parser.add_argument("--ip", required=True, help="Modbus server IP")
    parser.add_argument("--port", required=True, help="Modbus server Port")
    parser.add_argument("--address", required=True, help="Register/Coil address")
    parser.add_argument("--count", default=1, help="Number of registers/coils to read")
    parser.add_argument("--value", help="Value to write (only for write commands)")

    args = parser.parse_args()

    if args.command == "read_coil":
        read_coil(args.ip, args.port, args.address, args.count)
    elif args.command == "write_coil":
        if args.value is None:
            print("Error: --value is required for write_coil")
        else:
            write_coil(args.ip, args.port, args.address, args.value)
    elif args.command == "read_register":
        read_register(args.ip, args.port, args.address, args.count)
    elif args.command == "write_register":
        if args.value is None:
            print("Error: --value is required for write_register")
        else:
            write_register(args.ip, args.port, args.address, args.value)

if __name__ == "__main__":
    main()