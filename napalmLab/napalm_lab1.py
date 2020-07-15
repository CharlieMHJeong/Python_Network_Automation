from napalm import get_network_driver
import json

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'cisco', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
ios_output = json.dumps(ios_output, indent=4)
print(ios_output)

ios_output = iosvl2.get_interfaces()
ios_output = json.dumps(ios_output, sort_keys=True, indent=4)
print(ios_output)

ios_output = iosvl2.get_interfaces_counters()
ios_output = json.dumps(ios_output, sort_keys=True, indent=4)
print(ios_output)
