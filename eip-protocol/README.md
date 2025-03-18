# EIP Protocol Enumeration

This Python CLI tool allows you to interact with a PLC using the EtherNet/IP protocol. You can enumerate all available tags, read the value of a specific tag, and write a value to a tag—all from the command line.

## Features ✨

- :electric_plug: **PLC Tag Enumeration:** Connects to a PLC and retrieves a list of all available tags.
- :eyes: **Read Tag:** Reads the current value of a specified tag from the PLC.
- :pencil2: **Write Tag:** Writes a new value to a specified tag on the PLC.
- :keyboard: **Simple CLI Interface:** Easily execute commands directly from your terminal using straightforward parameters.

## Prerequisites 🛠️

- Python 3.x
- [pycomm3](https://pypi.org/project/pycomm3/)

## Installation 📥

1. **Install Python 3:** Ensure that Python 3 is installed on your system.
2. **Install pycomm3:** Use pip to install the required package:

   ```bash
   pip install pycomm3
   ```

3. **Clone the Repository:** Download or clone this repository to your local machine.

## Usage 🏃

Run the script using Python 3 with the appropriate command and parameters. The general command format is:

```bash
python3 eip_client.py <PLC_IP> <command> [<args>]
```

### Commands

- **enum:** Enumerate all available tags on the PLC.
  
  ```bash
  python3 eip_client.py <PLC_IP> enum
  ```

- **read:** Read the value of a specific tag.
  
  ```bash
  python3 eip_client.py <PLC_IP> read <TAG_NAME>
  ```

- **write:** Write a value to a specific tag.
  
  ```bash
  python3 eip_client.py <PLC_IP> write <TAG_NAME> <VALUE>
  ```

## Examples 🚀

- **Enumerate All Tags:**

  ```bash
  python3 eip_client.py 192.168.1.10 enum
  ```

  This command connects to the PLC at IP `192.168.1.10` and lists all available tags along with their data type and address.

- **Read a Specific Tag:**

  ```bash
  python3 eip_client.py 192.168.1.10 read MotorSpeed
  ```

  This command reads the value of the tag `MotorSpeed` from the PLC.

- **Write to a Specific Tag:**

  ```bash
  python3 eip_client.py 192.168.1.10 write MotorSpeed 1500
  ```

  This command writes the value `1500` to the `MotorSpeed` tag on the PLC. The script attempts to convert the value to a number (integer or float) if possible.

## Code Overview 📂

- **enumerate_plc(plc_ip):**  
  Connects to the PLC using the provided IP address, retrieves the tag list, and prints each tag's name, data type, and symbol address.

- **read_tag(plc_ip, tag_name):**  
  Reads and displays the value of the specified tag from the PLC.

- **write_tag(plc_ip, tag_name, value):**  
  Writes the given value to the specified tag on the PLC. The script attempts to convert the value to a numeric type if possible.

- **Command-Line Interface:**  
  The script uses command-line arguments to determine which operation to perform. It supports three commands: `enum`, `read`, and `write`.

## Error Handling 📝

- The tool prints error messages if it encounters issues when connecting to the PLC or performing read/write operations.
- Verify that the PLC IP is correct and that the PLC supports EtherNet/IP communications.

## License 📄

This tool is provided "as is" without any warranties. Use it at your own risk.