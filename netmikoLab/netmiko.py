
#!/usr/bin/env python3

from netmiko import ConnectHandler

with open('commands_file') as f:
        commands_to_send = f.read().splitlines()

with open('devices_file') as f:
        devices_list = f.read().splitlines()

for devices in devices_list:
        print("Connecting to Device ", devices)
        ip_address_of_device = devices
        ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'cisco',
        'password': 'cisco',
        }

        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(commands_to_send)
        print(output)
