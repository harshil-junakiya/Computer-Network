class Switch:
    def __init__(self):
        self.connectedDevices = []

    def connect(self, device):
        self.connectedDevices.append(device)

    def getConnectedDevices(self):
        return self.connectedDevices