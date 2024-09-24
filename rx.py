"""
This script sets up an XBee device to receive data from a remote XBee device.
Modules:
    digi.xbee.devices: Provides classes for XBee device communication.
Classes:
    XBeeDevice: Represents an XBee device.
    XBee64BitAddress: Represents a 64-bit address of an XBee device.
    RemoteXBeeDevice: Represents a remote XBee device.
Functions:
    data_received_callback(message): Callback function that processes received data.
Usage:
    - Initialize the XBee device with the specified COM port and baud rate.
    - Define the source address of the remote XBee device.
    - Open the XBee device.
    - Create a RemoteXBeeDevice instance with the source address.
    - Add a data received callback to the XBee device.
    - Continuously read data from the remote XBee device until interrupted.
    - Close the XBee device upon termination.
Example:
    Run the script to start receiving data from the remote XBee device.
"""

from digi.xbee.devices import XBeeDevice, XBee64BitAddress, RemoteXBeeDevice

device = XBeeDevice("COM5", 9600)
src_address = XBee64BitAddress.from_hex_string("0013A200422B138D")

def data_received_callback(message):
    address = message.remote_device.get_64bit_addr()
    data = message.data.decode("utf8")
    
    print("Received data from %s: %s" % (address, data))

device.open()

remote = RemoteXBeeDevice(device, src_address)

device.add_data_received_callback(data_received_callback)

while True:
    try:
        message = device.read_data_from(remote)
    except KeyboardInterrupt:
        print("Done")
        break

device.close()