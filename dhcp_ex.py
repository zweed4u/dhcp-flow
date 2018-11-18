#!/usr/bin/python3
# DHCP discover - broadcast from host
# DHCP offer - Server responds with possible assignment
# DHCP request - Host agrees and requests that
# DHCP ack - Server confirms and provides information - ip address, subnet mask, default gateway and dns server


class NetworkDevice:
    def __init__(self, name):
        self.name = name


class DHCPServer(NetworkDevice):
    # TODO flush out methods - in steps
    def __init__(self, name):
        super().__init__(name)
        self.udp_port = 67

    def offer(self):
        pass

    def ack(self):
        pass


class Router(DHCPServer):
    def __init__(self, name):
        super().__init__(name)


class Switch(NetworkDevice):
    def __init__(self, name):
        super().__init__(name)


class DHCPHost(NetworkDevice):
    # client
    def __init__(self, name, state, has_ip):
        super().__init__(name)
        self.state = state
        self.has_ip = has_ip
        self.broadcasting = False
        self.udp_port = 68

    def broadcast_discover(self):
        #print('I NEED AN IP')
        self.broadcasting = True


class PC(DHCPHost):
    def __init__(self, name, state, has_ip):
        super().__init__(name, state, has_ip)

    def power_on(self):
        if self.state.upper() == 'ON':
            print('PC already on!')
        else:
            self.state = 'ON'
        return True

    def get_ip(self):
        if self.has_ip:
            print('PC already has ip address')
        else:
            self.broadcast_discover()


# General network topology
router = Router('r1')
switch = Switch('s1')
PC1 = PC('pc1', 'OFF', False)  # running some DHCP client
PC2 = PC('pc2', 'ON', True)    # running some DHCP client

all_devices = [router, switch, PC1, PC2]

for device in all_devices:
    print(device.name)

hosts = [PC1, PC2]
server = router

PC1.power_on()
PC1.get_ip()

for host in hosts:
    if host.broadcasting:
        print(f'{host.name} is broadcasting that it needs an ip address. (DHCP discover)')
