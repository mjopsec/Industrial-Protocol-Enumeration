import argparse
import time
import random
from pydnp3 import opendnp3, asiopal, asiodnp3, openpal

# List of common Group/Variation in the DNP3 protocol
COMMON_GROUP_VARIATIONS = [
    (1, 2),   # Binary Input
    (2, 1),   # Binary Output
    (10, 2),  # Analog Input
    (20, 1),  # Counter
    (30, 1),  # Frozen Counter
    (40, 1)   # Device Attributes
]

class DNP3Fuzzer:
    def __init__(self, host, port, enable_fuzz=False):
        self.host = host
        self.port = int(port)
        self.enable_fuzz = enable_fuzz
        self.data_found = False  # Flag to check if data is found

        # Create DNP3 Manager with logging
        self.manager = asiodnp3.DNP3Manager(1, asiodnp3.ConsoleLogger())

        # Create TCP Client
        self.channel = self.manager.AddTCPClient(
            "client",
            0,  # Logging level (0 = disable logs)
            asiopal.ChannelRetry.Default(),
            str(self.host),
            "",
            self.port,
            asiodnp3.PrintingChannelListener()
        )

        if not self.channel:
            print "[!] Failed to create DNP3 channel"
            return

        # Configure Master
        stack_config = asiodnp3.MasterStackConfig()
        stack_config.master.responseTimeout = openpal.TimeDuration.Milliseconds(5000)
        stack_config.link.LocalAddr = 1
        stack_config.link.RemoteAddr = 100

        # Create Master
        self.master = self.channel.AddMaster(
            "master",
            asiodnp3.PrintingSOEHandler(),
            asiodnp3.DefaultMasterApplication(),
            stack_config
        )

        print "[*] Connecting to DNP3 server {}:{}".format(self.host, self.port)

    def start(self):
        if self.master:
            self.master.Enable()
            print "[*] DNP3 Master enabled."
        else:
            print "[!] Failed to enable master."

    def scan_common_groups(self):
        print "[*] Scanning common Group-Variations..."
        for group, variation in COMMON_GROUP_VARIATIONS:
            if self.send_scan(group, variation):
                self.data_found = True  # Set flag if a response is received
        print "[*] Common Group-Variation scan complete."

    def fuzz(self):
        if self.data_found:
            print "[*] Data has been found in common Group-Variations, no fuzzing needed."
            return

        print "[*] No data from common Group-Variations, starting fuzzing..."
        for group in xrange(0, 101):  # Test Groups 0 - 100
            for variation in xrange(0, 10):  # Test Variations 0 - 9
                self.send_scan(group, variation)
        print "[*] Fuzzing complete."

    def send_scan(self, group, variation):
        print "[*] Trying Group {}, Variation {}...".format(group, variation)
        try:
            # Correct call to AllObjects()
            header = list([opendnp3.Header().AllObjects(group, variation)])
            task_config = opendnp3.TaskConfig.Default()

            self.master.Scan(header, task_config)
            time.sleep(0.5)  # Delay to avoid flooding the server
            return True
        except Exception as e:
            print "[!] Error during scan of Group {}, Variation {}: {}".format(group, variation, e)
            return False

    def write_data(self, group, variation, index, value):
        """
        Function to write data to the DNP3 Server
        """
        print "[*] Writing to DNP3 Server - Group {}, Variation {}, Index {}, Value {}".format(group, variation, index, value)
        try:
            if group == 10:  # Analog Input
                command = opendnp3.AnalogCommand(value)
                self.master.DirectOperate(
                    command,
                    opendnp3.CommandPointState(opendnp3.CommandStatus.SUCCESS, index)
                )
            elif group == 2:  # Binary Output
                command = opendnp3.BinaryOutputStatus(True if value > 0 else False)
                self.master.DirectOperate(
                    command,
                    opendnp3.CommandPointState(opendnp3.CommandStatus.SUCCESS, index)
                )
            else:
                print "[!] Group {} is not supported for writing.".format(group)
                return False

            print "[*] Data successfully sent to DNP3 Server."
            return True
        except Exception as e:
            print "[!] Error while writing data: {}".format(e)
            return False

    def shutdown(self):
        self.manager.Shutdown()
        print "[*] DNP3 Fuzzer shutdown."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNP3 Group-Variation Scanner & Fuzzer")
    parser.add_argument("host", type=str, help="IP address of the DNP3 server")
    parser.add_argument("port", type=int, help="Port number of the DNP3 server")
    parser.add_argument("--fuzz", action="store_true", help="Enable fuzzing if no data is found from common groups")
    parser.add_argument("--write", nargs=4, metavar=('group', 'variation', 'index', 'value'), type=str,
                        help="Write data to the DNP3 server with format: --write <group> <variation> <index> <value>")
    args = parser.parse_args()

    client = DNP3Fuzzer(args.host, args.port, enable_fuzz=args.fuzz)
    client.start()

    try:
        if args.write:
            group = int(args.write[0])
            variation = int(args.write[1])
            index = int(args.write[2])
            value = float(args.write[3])
            client.write_data(group, variation, index, value)
        else:
            client.scan_common_groups()
            if args.fuzz:
                client.fuzz()
    finally:
        client.shutdown()
