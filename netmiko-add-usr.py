# Adding a user with netmiko

import netmiko

from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type="cisco_xe",
    host="192.168.1.135",
    username="cisco",
    password="cisco123!",
)

username = input("Provide username: ")
is_admin = input("Do you want the user to be an administrative user? (yes/no) ")
if is_admin == 'yes':
    privilege = 15
elif is_admin == 'no':
    privilege = 1
password = input("Provide user password: ")

net_connect.send_config_set(f"username {username} privilege {privilege} password {password}")
print(net_connect.send_command("show run | include user"))
