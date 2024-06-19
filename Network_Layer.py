import heapq

class Router:
    def __init__(self, name, network_layer):
        self.name = name
        self.networkLayer = network_layer
        self.interfaces = {}
        self.routingTable = RoutingTable()
        self.arpCache = {}
        self.rip = RIPProtocol(self)

    def addInterface(self, interface, ip_address, subnet_mask):
        self.interfaces[interface] = (ip_address, subnet_mask)
        self.routingTable.addRoute(ip_address, subnet_mask, interface, 0)

    def sendARPRequest(self, target_ip):
        pass

    def forwardPacket(self, packet, target_ip):
        if target_ip in self.arpCache:
            target_mac = self.arpCache[target_ip]
        else:
            self.sendARPRequest(target_ip)

    def addStaticRoute(self, network, subnet_mask, next_hop, interface):
        self.routingTable.addRoute(network, subnet_mask, next_hop, 1, interface)

class RoutingTable:
    def __init__(self):
        self.routes = []

    def addRoute(self, network, subnet_mask, next_hop, metric, interface=None):
        route = (network, subnet_mask, next_hop, metric, interface)
        self.routes.append(route)

    def findBestRoute(self, target_ip):
        best_route = None
        longest_mask = 0

        for network, subnet_mask, next_hop, metric, interface in self.routes:
            mask_len = sum(bin(int(subnet_mask.replace('.', '0b'), 2)).count('1'))
            if mask_len > longest_mask and ip_in_network(target_ip, network, subnet_mask):
                longest_mask = mask_len
                best_route = (next_hop, interface)

        return best_route

def ip_in_network(ip, network, subnet_mask):
    ip_addr = int(''.join([bin(int(x))[2:].zfill(8) for x in ip.split('.')]), 2)
    network_addr = int(''.join([bin(int(x))[2:].zfill(8) for x in network.split('.')]), 2)
    mask = int(''.join([bin(int(x))[2:].zfill(8) for x in subnet_mask.split('.')]), 2)
    return (ip_addr & mask) == (network_addr & mask)

class RIPProtocol:
    def __init__(self, router):
        self.router = router
        self.routingTable = router.routingTable
        self.neighbors = {}

    def addNeighbor(self, neighbor, interface):
        self.neighbors[neighbor] = interface

    def advertiseRoutes(self):
        advertisement = []
        for network, subnet_mask, next_hop, metric, interface in self.routingTable.routes:
            if metric < 16:
                advertisement.append((network, subnet_mask, metric + 1))

        for neighbor, interface in self.neighbors.items():
            pass

    def receiveRouteUpdate(self, neighbor, routes):
        for network, subnet_mask, metric in routes:
            if metric < 16:
                self.routingTable.addRoute(network, subnet_mask, neighbor, metric + 1)

    def runPeriodicUpdates(self):
        while True:
            self.advertiseRoutes()
            pass

class DHCP:
    def __init__(self, network_layer):
        self.networkLayer = network_layer
        self.availableIPs = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5"]

    def requestIP(self, device):
        if device in self.networkLayer.ipAddressTable:
            return

        if len(self.availableIPs) > 0:
            ip_address = self.availableIPs.pop(0)
            self.networkLayer.assignIPAddress(device, ip_address)
            print(f"Assigned IP address {ip_address} to {device.name}")
        else:
            print(f"No available IP addresses for {device.name}")

class NetworkLayer:
    def __init__(self):
        self.ipAddressTable = {}

    def assignIPAddress(self, device, ip_address):
        self.ipAddressTable[device] = ip_address

    def getIPAddress(self, device):
        return self.ipAddressTable.get(device, None)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


network_layer = NetworkLayer()
dhcp = DHCP(network_layer)

router1 = Router("Router1", network_layer)
router1.addInterface("eth0", "192.168.1.1", "255.255.255.0")
router1.addInterface("eth1", "10.0.0.1", "255.255.255.0")

router2 = Router("Router2", network_layer)
router2.addInterface("eth0", "192.168.2.1", "255.255.255.0")
router2.addInterface("eth1", "10.0.0.2", "255.255.255.0")

router1.addStaticRoute("192.168.2.0", "255.255.255.0", "10.0.0.2", "eth1")
router2.addStaticRoute("192.168.1.0", "255.255.255.0", "10.0.0.1", "eth1")

router1.rip.addNeighbor("10.0.0.2", "eth1")
router2.rip.addNeighbor("10.0.0.1", "eth1")

router1.rip.runPeriodicUpdates()
router2.rip.runPeriodicUpdates()


dhcp.requestIP(router1)
dhcp.requestIP(router2)


best_route = router1.routingTable.findBestRoute("192.168.2.10")
print(f"Best route from Router1 to 192.168.2.10: {best_route}")


graph = {
    "Router1": {"Router2": 1},
    "Router2": {"Router1": 1}
}
distances = dijkstra(graph, "Router1")
print(f"Shortest path from Router1 to Router2: {distances['Router2']}")