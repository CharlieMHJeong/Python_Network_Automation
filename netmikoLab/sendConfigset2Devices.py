#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

#get username and pw from the user inputs
user = input("Please enter username: ")
pw = getpass()

#open devices file list to put in devices list
with open('devices_file', 'r') as f:
    devices = f.read().splitlines()

with open('commands_file') as f:
    commands = f.read().splitlines()

#go through each device in devices list
for device in devices:
    print("Processing {}".format(device))
    ios_device = {
            'device_type': 'cisco_ios',
            'ip': device,
            'username': user,
            'password': pw,
            }
    conn = ConnectHandler(**ios_device)
    r = conn.send_config_set(commands)
    print(r)
