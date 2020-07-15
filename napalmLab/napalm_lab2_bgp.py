from napalm import get_network_driver
import json

bgplist = ['192.168.122.72', '192.168.122.71']

for ip_address in bgplist:
    print("Connecting ==> ", ip_address)
    driver = get_network_driver('ios')
    iosvrouter = driver(ip_address, 'cisco', 'cisco')
    iosvrouter.open()

    bgp_neighbors = iosvrouter.get_bgp_neighbors()
    bgp_neighbors = json.dumps(bgp_neighbors, indent=4)
    print(bgp_neighbors)

    iosvrouter.close()
