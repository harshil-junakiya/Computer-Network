import socket

class ApplicationLayer:
    def __init__(self, device, transport_layer):
        self.device = device
        self.transport_layer = transport_layer

    def sendHTTPRequest(self, destination, path):
        print("Entering sendHTTPRequest function")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            destination_ip = destination.ip_address
            destination_port = self.transport_layer.getPort(destination)
            sock.connect((destination_ip, destination_port))

            request = f"GET {path} HTTP/1.1\r\nHost: {destination_ip}\r\n\r\n"
            sock.sendall(request.encode())

            response = sock.recv(1024).decode()

            print(f"Received response from {destination.getName()}: {response}")

        except ConnectionRefusedError:
            print(f"Connection refused: Unable to connect to {destination.getName()}")

        except Exception as e:
            print(f"An error occurred while sending the HTTP request to {destination.getName()}: {str(e)}")

        finally:
            sock.close()

        print("Exiting sendHTTPRequest function")

    def sendDNSRequest(self, dns_server, hostname):
        print("Entering sendDNSRequest function")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dns_server_ip = dns_server.ip_address
            dns_server_port = self.transport_layer.getPort(dns_server)
            request = f"{hostname}"
            sock.sendto(request.encode(), (dns_server_ip, dns_server_port))

            response, _ = sock.recvfrom(1024)
            response = response.decode()

            print(f"Received DNS response from {dns_server.getName()}: {response}")

        except Exception as e:
            print(f"An error occurred while sending the DNS request to {dns_server.getName()}: {str(e)}")

        finally:
            sock.close()

        print("Exiting sendDNSRequest function")
