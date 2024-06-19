import random

class GoBackN:
    def __init__(self, window_size):
        self.window_size = window_size
        self.base = 0
        self.next_seq_num = 0
        self.buffer = {}
        self.ack_expected = 0

    def send_data(self, data):
        while self.next_seq_num < self.base + self.window_size:
            frame = self.make_frame(self.next_seq_num, data)
            self.buffer[self.next_seq_num] = frame
            self.next_seq_num += 1


    def make_frame(self, seq_num, data):
        return f"Frame {seq_num}: {data}"

    def receive_ack(self, ack_num):
        if ack_num >= self.ack_expected:
            self.base = ack_num + 1
            self.ack_expected += 1
            for seq_num in range(self.base - self.window_size, self.base):
                self.buffer.pop(seq_num, None)

    def receive_nak(self, nak_num):
        self.base = nak_num
        self.next_seq_num = self.base + self.window_size


class TransportLayer:
    def __init__(self):
        self.portTable = {}
        self.flow_control = GoBackN(window_size=4)  

    def openPort(self, device, port):
        self.portTable[device] = port

    def getPort(self, device):
        return self.portTable.get(device, None)

    def send_data(self, data):
        self.flow_control.send_data(data)

    def receive_ack(self, ack_num):
        self.flow_control.receive_ack(ack_num)

    def receive_nak(self, nak_num):
        self.flow_control.receive_nak(nak_num)