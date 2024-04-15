import time

class SelectiveRepeatARQ:
    def __init__(self, window_size):
        self.window_size = window_size

    def send_data(self, data, devices, source_device):
        start = time.process_time()
        for i in range(0, len(data), self.window_size):
            window_frames = data[i:i+self.window_size]
            ack_received = [False] * len(window_frames)
            while not all(ack_received):
                for j in range(len(window_frames)):
                    if ack_received[j]:
                        continue

                    devices[(i + j) % len(devices)].data += window_frames[j]
                    print(f"Sent frame number: {i+j+1} to Device. {devices[(i+j) % len(devices)].name}")
                    print(f"Awaiting ACK for frame number: {i+j+1} at Device {devices[(i+j) % len(devices)].name}")
                    ack_received[j] = True  # Placeholder for ACK condition, modify as needed

                    if not ack_received[j]:
                        print(f"ACK not received for frame number: {i+j+1} at Device {devices[(i+j) % len(devices)].name}, retransmitting...")

        time_taken = time.process_time() - start
        print()
        print("*******************************************************")
        print("Total Time Taken for Transmission:", time_taken)

