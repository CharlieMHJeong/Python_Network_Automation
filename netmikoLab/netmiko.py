#!/usr/bin/env python3
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = input("Enter your SSH Username: ")
password = getpass()

with open('commands_file_switch') as f:
        commands_list_switch = f.read().splitlines()

with open('commands_file_router') as f:
        commands_list_router = f.read().splitlines()

with open('devices_file') as f:
        devices_list = f.read().splitlines()

for devices in devices_list:
        print("Connecting to Device ", devices)
        ip_address_of_device = devices
        ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password,
        }

        try:
                net_connect = ConnectHandler(**ios_device)
        except(AuthenticationException):
                print("Authentication Failure: " + ip_address_of_device)
                continue
        except(NetMikoTimeoutException):
                print("Timeout to Device : " + ip_address_of_device)
                continue
        except(EOFError):
                print("End of file while attempting device : " + ip_address_of_device)
                continue
        except(SSHException):
                print("SSH Issue. Are you sure SSH is enabled? " + ip_address_of_device)
                continue
        except(Exception) as unknown_error:
                print("Some other Error: unknown_error" + ip_address_of_device)
                continue

        #Types of devices
        list_versions = ['vios_l2-adventerprisek9-m',
                         'VIOS-ADVENTERPRISEK9-M',
                         'C1900-UNIVERSAL9-M',
                         'C3750-ADVENTERPRISEK9-M']

        #Check Software Versions
        for software_ver in list_versions:
                print("Checking for " + software_ver)
                output_version = net_connect.send_command('show version')
                int_version = 0 #Reset integer values
                int_version = output_version.find(software_ver) #Check software_ver
                if int_version > 0:
                        print("Software version found: " + software_ver)
                        break
                else:
                        print("Did not find" + software_ver)

        if software_ver == 'vios_l2-adventerprisek9-m':
                print("Running " + software_ver + " commands")
                output = net_connect.send_config_set(commands_list_switch)
        elif software_ver == 'VIOS-ADVENTERPRISEK9-M':
                print("Running " + software_ver + " commands")
                output = net_connect.send_config_set(commands_list_router)
        elif software_ver == 'C1900-UNIVERSAL9-M':
                print("Running " + software_ver + " commands")
                output = net_connect.send_config_set(commands_list_router)
        elif software_ver == 'C3750-ADVENTERPRISEK9-M':
                print("Running " + software_ver + " commands")
                output = net_connect.send_config_set(commands_list_switch)
        print(output)
