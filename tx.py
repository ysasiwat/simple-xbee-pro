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
    