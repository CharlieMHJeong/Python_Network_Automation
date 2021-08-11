from textfsm import TextFSM
from netmiko import ConnectHandler
from getpass import getpass
from pandas import DataFrame
from tabulate import tabulate
from io import StringIO

#Get login detais from User input
USERNAME = input("Please enter username:")
PASSWORD = getpass()
#print("U: {}, P: {}".format(USERNAME, PASSWORD))

#Read template from a file and store to a var - template
with open("showiproute.template", 'rt') as f:
    template = f.read()

#Read device list to put in a list - devices
with open("devices_file", 'rt') as f:
    devices = f.read().splitlines()

#Go through devices 
for device in devices:
    device_details ={
                    'device_type': 'cisco_ios',
                    'ip': device,
                    'username': USERNAME,
                    'password': PASSWORD,
                     }

    conn = ConnectHandler(**device_details)
    shiproute = conn.send_command('show ip route')
    #print(shiproute)
    print("--  ----------  ------  --------------  ------  ----------  --------  ------------  ------------------  --------")
    print("Processing device: {}".format(device))
    print("--  ----------  ------  --------------  ------  ----------  --------  ------------  ------------------  --------")
    parser = TextFSM(StringIO(template))
    hdrs, vals = parser.header, parser.ParseText(shiproute)
    df = DataFrame(vals, columns = hdrs)
    print(tabulate(df, headers=hdrs))
    df.to_csv("{}.csv".format(device))
    print("--  ----------  ------  --------------  ------  ----------  --------  ------------  ------------------  --------")
    print()
    print()
    print()
