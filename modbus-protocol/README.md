# Modbus Protocol Enumeration

This Python CLI tool allows you to interact with a Modbus TCP server. You can read and write coils or registers using simple command-line arguments. Whether you're troubleshooting or performing automation tasks, this tool is designed to be straightforward and effective.

## Features ✨

- :electric_plug: **Modbus TCP Connection:** Connects to a Modbus server using the provided IP address and port.
- :mag: **Read Coils/Registers:** Retrieve the status of coils or the values of holding registers.
- :wrench: **Write Coils/Registers:** Write values to coils or registers.
- :keyboard: **Simple CLI Interface:** Easily specify the target address, count, and values using command-line arguments.

## Prerequisites 🛠️

- Python 3.x
- [pymodbus](https://pypi.org/project/pymodbus/)


## Installation 📥

1. Ensure you have Python 3 installed.
2. Install the `pymodbus` package using pip:

   ```bash
   pip install pymodbus
   ```

3. Download or clone this repository to your local machine.


## Usage 🏃

Run the script using Python 3 along with the required arguments. The basic command format is:

```bash
python3 modbus.py <command> --ip <IP> --port <Port> --address <Address> [--count <Count>] [--value <Value>]
```

### Available Commands

- **read_coil:** Reads coils from the specified address.
- **write_coil:** Writes a boolean value to the specified coil address.
- **read_register:** Reads holding registers from the specified address.
- **write_register:** Writes a numeric value to the specified register address.

## Examples 🚀

- **Read Coils:**  
  To read 10 coils starting from address 10:
  
  ```bash
  python3 modbus.py read_coil --ip 172.23.1.1 --port 502 --address 10 --count 10
  ```

- **Write Coil:**  
  To write the value `1` (True) to the coil at address 10:
  
  ```bash
  python3 modbus.py write_coil --ip 172.23.1.1 --port 502 --address 10 --value 1
  ```

- **Read Registers:**  
  To read 10 holding registers starting from address 10:
  
  ```bash
  python3 modbus.py read_register --ip 172.23.1.1 --port 502 --address 10 --count 10
  ```

- **Write Register:**  
  To write the value `1234` to the register at address 10:
  
  ```bash
  python3 modbus.py write_register --ip 172.23.1.1 --port 502 --address 10 --value 1234
  ```

## Code Structure 📂

- **read_coil:**  
  Connects to the Modbus server and reads a specified number of coils starting at a given address. It prints each coil's status.

- **write_coil:**  
  Connects to the Modbus server and writes a boolean value to the specified coil address.

- **read_register:**  
  Connects to the Modbus server and reads a specified number of holding registers, printing each register's value.

- **write_register:**  
  Connects to the Modbus server and writes a numeric value to the specified register address.

- **main():**  
  Parses command-line arguments and calls the appropriate function based on the chosen command.

## Notes 📝

- Ensure that the Modbus server is accessible from your network and that the specified IP and port are correct.
- The `--count` parameter is optional and defaults to 1 if not specified.
- The `--value` parameter is required only for write commands (`write_coil` and `write_register`).


## License 📄

This tool is provided "as is" without any warranties. Use it at your own risk.