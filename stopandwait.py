import time

class StopAndWaitARQ:
    def send_data(self, data, devices, source_device):
        start = time.process_time()
        for i in range(len(data)):
            if devices[i % len(devices)] == source_device:
                continue

            # Send the data frame and wait for ACK
            ack_received = False
            while not ack_received:
                devices[i % len(devices)].data += data[i]
                print(f"Sent frame number: {i+1} to Device {devices[i % len(devices)].name}")
                print(f"Awaiting ACK for frame number: {i+1} at Device {devices[i % len(devices)].name}")
                ack_received = True  # Placeholder for ACK condition, modify as needed

                if not ack_received:
                    print(f"ACK not received for frame number: {i+1} at Device {devices[i % len(devices)].name}, retransmitting...")

            print(f"ACK received for frame number: {i+1} at Device {devices[i % len(devices)].name}")

        time_taken = time.process_time() - start
        print()
        print("*******************************************************")
        print("Total Time Taken for Transmission:", time_taken)
