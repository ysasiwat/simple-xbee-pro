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