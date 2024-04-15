class Hub:
    def __init__(self,name):
        self.name = name
        self.data2 = "0"
        self.macAdd = 0
        self.connectedDevices = []

    def store(self, SD_Data, sourceDevice, devMACaddress):
        self.data2 = SD_Data
        self.macAdd = devMACaddress
        self.hub2dev(self.data2, sourceDevice, self.macAdd)

    def connect(self, device):
        self.connectedDevices.append(device)

    def getConnectedDevices(self):
        device_names = []
        for device in self.connectedDevices:
            device_names.append(device.name) 
        return device_names
    

    def hub2dev(self, data2, sourceDevice, macAdd):
        print()
        print("*******************************************************")
        if A.MACaddress == macAdd and A.data == data2 and sourceDevice != "A":
            print("A Accepted the Data and the Received data is:", data2)
        else:
            if sourceDevice != "A":
                print("Data doesn't belong to A")

        if B.MACaddress == macAdd and B.data == data2 and sourceDevice != "B":
            print("B Accepted the Data and the Received data is:", data2)
        else:
            if sourceDevice != "B":
                print("Data doesn't belong to B")

        if C.MACaddress == macAdd and C.data == data2 and sourceDevice != "C":
            print("C Accepted the Data and the Received data is:", data2)
        else:
            if sourceDevice != "C":
                print("Data doesn't belong to C")

        if D.MACaddress == macAdd and D.data == data2 and sourceDevice != "D":
            print("D Accepted the Data and the Received data is:", data2)
        else:
            if sourceDevice != "D":
                print("Data doesn't belong to D")

        if E.MACaddress == macAdd and E.data == data2 and sourceDevice != "E":
            print("E Accepted the Data and the Received data is:", data2)
        else:
            if sourceDevice != "E":
                print("Data doesn't belong to E")

        print()


class Device:
    def __init__(self, name):
        self.name = name
        self.data = ""
        self.MACaddress = ""
        self.ipAddress = ""
        self.port = 0

    def setMACaddress(self, MAC):
        self.MACaddress = MAC

    def setData(self, dat):
        self.data = dat

    def setIPAddress(self, ipAddress):
        self.ipAddress = ipAddress

    def getIPAddress(self):
        return self.ipAddress

    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port

    def getName(self):
        return self.name


    

    


A = Device("A")
B = Device("B")
C = Device("C")
D = Device("D")
E = Device("E")
hb1 = Hub("hub1")



def deviceInfo():
    # here, I am initializing Devices.

    
    A.setData("0")
    B.setData("0")
    C.setData("0")
    D.setData("0")
    E.setData("0")
    A.setMACaddress("00:1A:2B:3C:4D:5E")
    B.setMACaddress("08:00:27:3F:A0:C9")
    C.setMACaddress("34:23:87:9E:FA:B2")
    D.setMACaddress("AB:CD:EF:12:34:56")
    E.setMACaddress("52:54:00:12:34:AB")

def getMACTable():
    print("MAC Table:")
    print("MACAddress of A:", A.MACaddress)
    print("MACAddress of B:", B.MACaddress)
    print("MACAddress of C:", C.MACaddress)
    print("MACAddress of D:", D.MACaddress)
    print("MACAddress of E:", E.MACaddress)
    print()
    
        

deviceInfo()

