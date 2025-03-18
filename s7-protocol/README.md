# S7 Protocol Enumeration

This tool is a simple Python client that connects to a Siemens S7 PLC using the Snap7 library. It automatically attempts to connect using a list of common rack/slot combinations, retrieves basic PLC information, scans for available Data Blocks (DB), and reads data from them.

## Features

- **Automatic Connection:** Attempts connection to a PLC using common rack/slot combinations.
- **PLC Information Retrieval:** Fetches and displays key PLC information such as order code, CPU model, serial number, and CPU state.
- **Data Block Scanning:** Scans the PLC for available Data Blocks (DB).
- **Data Reading:** Reads and displays integer, float, and boolean values from found Data Blocks.

## Prerequisites

- **Python 3.x**
- [Snap7](https://github.com/gijzelaerr/python-snap7) library

## Installation

1. **Clone or Download the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install the Required Library:**

   Install Snap7 for Python using pip:

   ```bash
   pip install python-snap7
   ```

   > **Note:** Ensure that your environment is properly configured to use the Snap7 library. Refer to the [Snap7 documentation](https://github.com/gijzelaerr/python-snap7) for further details.

## Usage

Run the script with the PLC's IP address as an argument:

```bash
python s7_client.py <PLC_IP>
```

### Example

```bash
python s7_client.py 192.168.0.10
```

**Workflow:**

1. **Connecting:** The script attempts to connect to the PLC using several common rack/slot configurations.
2. **Information Retrieval:** If connected, it retrieves and prints the PLC's order code, CPU model, serial number, AS name, module name, and CPU state.
3. **Data Block Scan:** It scans the PLC for available Data Blocks (DB) and lists the number of available DBs.
4. **Data Reading:** For each detected DB, the script reads a sample of data (integer, float, boolean) and displays the values.
5. **Disconnect:** Finally, the connection to the PLC is closed.

## Code Overview

- **`connect_plc(ip)`**  
  Attempts to establish a connection to the PLC using common rack/slot pairs. Returns the connected client along with the rack and slot used.

- **`get_plc_info(client)`**  
  Retrieves and prints basic information from the PLC, including the order code, CPU details, and CPU state.

- **`scan_data_blocks(client, max_db=10)`**  
  Scans for available Data Blocks (DB) by attempting to read from DB 1 to DB `max_db` and returns a list of detected DBs.

- **`read_data_from_dbs(client, dbs)`**  
  Reads and prints sample data (integer, float, boolean) from each available Data Block.

- **`main()`**  
  The main entry point that parses command-line arguments, connects to the PLC, retrieves information, scans Data Blocks, reads data, and then disconnects.

## License

This tool is provided "as is" without any warranties. Use it at your own risk.