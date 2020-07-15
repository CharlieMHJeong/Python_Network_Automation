# Config Cisco Devcie with napalm
napalm_config.py

## Getting Started
If the config in the device is different from the cfg file, it will commit the config other wise will discard the config.

### Requirements
1. Enable scp on the devices:<br/>
   ip scp server enable<br/>
2. For example 'ACL1.cfg' and 'ospf1.cfg' created for the script<br/>
   ACL1.cfg<br/>
   access-list 100 permit icmp any any<br/>
   access-list 100 permit tcp any any eq domain<br/>
   access-list 100 permit tcp any any eq www<br/>
   access-list 100 permit tcp any any eq 443<br/>

   ospf1.cfg:<br/>
   router ospf 1<br/>
     network 10.1.1.0 0.0.0.255 area 1<br/>
     network 10.1.2.0 0.0.0.255 area 2<br/>
     network 10.1.3.0 0.0.0.255 area 3<br/>

### Imported Libraries
from napalm import get_network_driver<br/>
