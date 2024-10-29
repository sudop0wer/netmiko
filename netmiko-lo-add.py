# Creating a Loopback interface and assigning an IP address with netmiko

import netmiko

from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.1.135",
    username="cisco",
    password="cisco123!",
)

command_list = [
    "interface lo 30",
    "ip add 10.10.30.3 255.255.255.255",
    "description created_with_netmiko",
    "no shut"
    "do write"
]

net_connect.send_config_set(command_list)
print(net_connect.send_command("show ip int br"))
print(net_connect.send_command("show interface lo 20"))
