from simplecrypt import encrypt, decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time

#------------------------------------------------------------------------------
def read_devices(devices_filename):

    #Dictionary created for storing devices and their info
    devices = {}

    with open(devices_filename) as devices_file:
        for device_line in devices_file:
            #Extract device info from line
            device_info = device_line.strip().split(',')

            #Create dict of device objects
            device = {'ipaddr': device_info[0],
                      'type': device_info[1],
                      'name': device_info[2] }

            #store device in the devices dictionary
            #note the key for devices dict entries
            devices[device['ipaddr']] = device

    print("\n----- devices --------------------------------")
    pprint(devices)

    return devices
#------------------------------------------------------------------------------
def read_device_creds(device_creds_filename, key):

    print("\n... getting credentials ...\n")
    with open(device_creds_filename, 'rb') as device_creds_file:
        device_creds_json = decrypt(key, device_creds_file.read())

    device_creds_list = json.loads(device_creds_json)
    pprint(device_creds_list)

    print("\n ----- device_creds --------------------------------")

    #convert to dict of lists using dictionary comprehension
    device_creds = { dev[0]:dev for dev in device_creds_list}
    pprint(device_creds)

    return device_creds

#------------------------------------------------------------------------------
def config_worker(device, creds):

    #---- Connect to the device ----
    if   device['type'] == 'junos-srx': device_type = 'juniper'
    elif device['type'] == 'cisco-ios': device_type = 'cisco_ios'
    elif device['type'] == 'cisco-xr': device_type = 'cisco_xr'
    else: device_type = 'cisco_ios'

    print("---- Connecting to device {0}, username={1}, password={2}".format(device['ipaddr'], creds[1], creds[2]))
    #---- Connect to the device ----
    session = ConnectHandler(device_type=device_type,
                             ip=device['ipaddr'],
                             username=creds[1],
                             password=creds[2])

    if device_type == 'juniper':
        #---- Use CLI command to get configuration data from device
        print('---- Getting configs from Device')
        session.send_command('configure terminal')
        config_data = session.send_command('show configuration')

    if device_type == 'cisco_ios':
        #---- Use CLI command to get configuration data from device
        print('---- Getting configs from Device')
        config_data = session.send_command('show run')

    if device_type == 'cisco_xr':
        #---- Use CLI command to get configuration data from device
        print('---- Getting configs from Device')
        config_data = session.send_command('show configuration running-config')

    #---- Write out configs info to file
    #Create unique configuration
    config_filename = 'config-' + device[ipaddr]

    print("---- Writing configuration: ", config_filename)
    with open(config_filename, 'w') as config_out:
        config_out.write(config_data)
    session.disconnect()
    return

#=============================================================================
# ---- Main: Get Configuration
#=============================================================================

#Prepare cvs file devices-file
#192.168.122.72, cisco-ios, S1
#192.168.122.73, cisco-ios, S2
#192.168.122.74, cisco-ios, R1
#192.168.122.75, cisco-ios, R2

devices = read_devices( 'devices-file')
creds = read_device_creds('encrypted-device-creds', 'cisco')

starting_time = time()

print("\n ---- Begin get config sequential --------\n")
for ipaddr,device in devices.items():
    print("Getting config for: ", device)
    config_worker(device, creds[ipaddr])

print("\n ---- End get config sequential, elapsed time= ", time()-starting_time)
