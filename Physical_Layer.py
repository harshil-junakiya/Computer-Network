from Hub import *

def broadcastData(data, source_device):
    connected_devices = [A, B, C, D, E]  # Assuming A, B, C, D, E are objects representing connected devices
    for device in connected_devices:
        if device != source_device:
            device.setData(data)
            print("Data transmitted from {} to {}.".format(source_device.name, device.name))
            hb1.store(data, source_device.name, device.MACaddress)

def dedicatedConnection(source_device, destination_device, data):
    print("Establishing dedicated connection between {} and {}.".format(source_device.name, destination_device.name))
    source_device.setData("0")
    destination_device.setData(data)
    print("Data transmitted from {} to {}.".format(source_device.name, destination_device.name))
    hb1.store(data, source_device.name, destination_device.MACaddress)

def physicalLayer():
    deviceInfo()
    print("Devices we have: A, B, C, D, E")
    
    source_device_name = input("Choose SourceDevice:\n")
    source_device = None
    
    for device in [A, B, C, D, E]:
        if device.name == source_device_name:
            source_device = device
            break
    
    if source_device is None:
        print("Invalid SourceDevice")
        return
    
    data = input("SourceDevice Data Input for transmission (In binary format):\n")
    for digit in data:
        if digit not in '01':
            print("Invalid Data Format (Please enter in binary format)")
            return
    
    print("1: StarTopologyConnection 2: DedicatedNetworkConnection")
    connection_type = int(input("Choose your Connection Type:\n"))
    
    if connection_type == 1:
        broadcastData(data, source_device)
    elif connection_type == 2:
        print("Devices available for dedicated connection:")
        for device in [A, B, C, D, E]:
            if device != source_device:
                print(device.name)
        destination_device_name = input("Choose DestinationDevice for dedicated connection:\n")
        destination_device = None
        for device in [A, B, C, D, E]:
            if device.name == destination_device_name:
                destination_device = device
                break
        if destination_device is None or destination_device == source_device:
            print("Invalid DestinationDevice")
            return
        dedicatedConnection(source_device, destination_device, data)
    else:
        print("Invalid Connection Type")
        return
    
    print("\nDevicesData after Transmission:")
    for device in [A, B, C, D, E]:
        print("{} data after Transmission: {}".format(device.name, device.data))
    
    print()
    getMACTable()

    return data, source_device_name

