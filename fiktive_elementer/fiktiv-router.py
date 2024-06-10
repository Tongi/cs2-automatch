import psutil
import socket

def get_ip_addresses():
    ip_addresses = {'IPv4': None, 'IPv6': None}
    
    # Get the list of network interfaces
    interfaces = psutil.net_if_addrs()
    
    for interface_name, interface_addresses in interfaces.items():
        print(f"Interface: {interface_name}")  # Debugging line
        for address in interface_addresses:
            print(f"Address: {address}")  # Debugging line
            if address.family == socket.AF_INET:  # IPv4
                if not address.address.startswith('127.'):  # Exclude loopback addresses
                    ip_addresses['IPv4'] = address.address
                    print(f"IPv4 Address found: {address.address}")  # Debugging line
            elif address.family == socket.AF_INET6:  # IPv6
                if not address.address.startswith('::1'):  # Exclude loopback addresses
                    ip_addresses['IPv6'] = address.address
                    print(f"IPv6 Address found: {address.address}")  # Debugging line
    
    return ip_addresses

class Router:
    def __init__(self, router_config, ipv4=None, ipv6=None):
        self.router_config = router_config
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.dhcp_enabled = False
        self.firewall_enabled = False
        self.port_forwarding_rules = []

    def enable_dhcp(self):
        self.dhcp_enabled = True
        print("DHCP server enabled.")

    def configure_firewall(self):
        if self.ipv4 is not None or self.ipv6 is not None:
            self.firewall_enabled = True
            print("Firewall configured for IPv4 and/or IPv6.")
        else:
            print("Failed to configure firewall. No IP addresses provided.")
    
    def add_port_forwarding_rule(self, external_port, internal_ip, internal_port):
        rule = {
            'external_port': external_port,
            'internal_ip': internal_ip,
            'internal_port': internal_port
        }
        self.port_forwarding_rules.append(rule)
        print(f"Port forwarding rule added: {rule}")

    def show_config(self):
        print("Router Configuration:")
        print(f"IPv4: {self.ipv4}")
        print(f"IPv6: {self.ipv6}")
        print(f"DHCP Enabled: {self.dhcp_enabled}")
        print(f"Firewall Enabled: {self.firewall_enabled}")
        print("Port Forwarding Rules:")
        for rule in self.port_forwarding_rules:
            print(rule)

# Example usage:
router_config = {
    "ssid": "Marcus",
    "password": "sofabord1234"
}

# Get the IP addresses of the current computer
ip_addresses = get_ip_addresses()
print(f"Retrieved IP Addresses: {ip_addresses}")  # Debugging line
ipv4 = ip_addresses['IPv4']
ipv6 = ip_addresses['IPv6']

# Check if IP addresses were successfully retrieved
if ipv4 is None and ipv6 is None:
    print("No IP addresses found. Please check your network connection and try again.")
else:
    # Create a fictive router instance with the obtained IP addresses
    my_router = Router(router_config, ipv4, ipv6)
    my_router.enable_dhcp()
    my_router.configure_firewall()
    my_router.add_port_forwarding_rule(8080, "192.168.0.2", 80)
    my_router.show_config()
