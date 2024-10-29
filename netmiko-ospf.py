# Opening OSPF process with netmiko

import netmiko

from netmiko import ConnectHandler

subnet_to_wildcard = {
    0: "255.255.255.255",
    1: "127.255.255.255",
    2: "63.255.255.255",
    3: "31.255.255.255",
    4: "15.255.255.255",
    5: "7.255.255.255",
    6: "3.255.255.255",
    7: "1.255.255.255",
    8: "0.255.255.255",
    9: "0.127.255.255",
    10: "0.63.255.255",
    11: "0.31.255.255",
    12: "0.15.255.255",
    13: "0.7.255.255",
    14: "0.3.255.255",
    15: "0.1.255.255",
    16: "0.0.255.255",
    17: "0.0.127.255",
    18: "0.0.63.255",
    19: "0.0.31.255",
    20: "0.0.15.255",
    21: "0.0.7.255",
    22: "0.0.3.255",
    23: "0.0.1.255",
    24: "0.0.0.255",
    25: "0.0.0.127",
    26: "0.0.0.63",
    27: "0.0.0.31",
    28: "0.0.0.15",
    29: "0.0.0.7",
    30: "0.0.0.3",
    31: "0.0.0.1",
    32: "0.0.0.0"
}


net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.1.135",
    username="cisco",
    password="cisco123!",
)

process_id = input("Please provide a process ID: ")
area_id = input("Please provide an area ID: ")

interfaces = {}
while True:
    interface = input("Please provide an interface IP address for which OSPF should be open (type 'exit' to end sequence): ")
    if interface == 'exit':
        break
    else:
        mask = input("Please provide a subnet mask for the interface (ex. 24 = /24): ")
    interfaces[interface] = mask

print(interfaces)

net_connect.send_config_set(f"ip ospf {process_id}")
for key in interfaces.keys():
    net_connect.send_config_set(f"network {key} {subnet_to_wildcard[int(interfaces[key])]} area {area_id}")

print(net_connect.send_command("show ip ospf"))