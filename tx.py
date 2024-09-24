"""
This script sends a message to a remote XBee device in an infinite loop with a delay of 10 seconds between each message.
Modules:
    digi.xbee.devices (XBeeDevice, XBee64BitAddress, RemoteXBeeDevice): Provides classes to interact with XBee devices.
    time: Provides time-related functions.
Usage:
    - Ensure the XBee device is connected to the specified COM port (COM6 in this case).
    - The destination XBee device address should be specified in the `dest_address` variable.
    - The message to be sent is specified in the `message` variable.
Functions:
    - device.open(): Opens the connection to the local XBee device.
    - device.send_data(remote, message): Sends the specified message to the remote XBee device.
    - device.close(): Closes the connection to the local XBee device.
    - time.sleep(10): Pauses the execution for 10 seconds.
Exception Handling:
    - KeyboardInterrupt: Catches the KeyboardInterrupt exception to allow graceful termination of the script.
Example:
    Sending data to 0013A200422B127D: Hello XBee World!
"""

from digi.xbee.devices import XBeeDevice, XBee64BitAddress, RemoteXBeeDevice
import time

device = XBeeDevice("COM6", 9600)
dest_address = XBee64BitAddress.from_hex_string("0013A200422B127D")
message = "Hello XBee World!"

while True:
    try:
        device.open()

        remote = RemoteXBeeDevice(device, dest_address)
        
        device.send_data(remote, message)
        print("Sending data to %s: %s" % (dest_address, message))

        device.close()

        time.sleep(10)
    except KeyboardInterrupt:
        print("Done")
        break
    