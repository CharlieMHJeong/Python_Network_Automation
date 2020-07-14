# Read Configs from Cisco Device with MultiThreading

## Getting Started
This application is going to read cisco device configurations.

### Requirements
1. Create 'encrypted-device-creds' encrypted login credential file from "encrypt_device_info.py"<br/>
2. CSV file 'devices-file' with IP, DeviceType, Hostname<br/>
   192.168.122.72, cisco-ios, S1<br/>
   192.168.122.73, cisco-ios, S2<br/>
   192.168.122.74, cisco-ios, R1<br/>
   192.168.122.75, cisco-ios, R2<br/>

### How To in Linux
1. python3 read_config_threadingpool.py<br/>
2. When prompted, enter number of threads that your system can support<br/>
   Number of thread(s) (5):<br/>
3. Check the config-files:<br/>
-rw-r--r-- 1 root root 4056 Jul 14 10:49 config-192.168.122.72<br/>
-rw-r--r-- 1 root root 4040 Jul 14 10:49 config-192.168.122.73<br/>
-rw-r--r-- 1 root root 3382 Jul 14 10:49 config-192.168.122.74<br/>
-rw-r--r-- 1 root root 3383 Jul 14 10:49 config-192.168.122.75<br/>


### Imported Libraries
from simplecrypt import encrypt, decrypt<br/>
from pprint import pprint<br/>
from netmiko import ConnectHandler<br/>
from multiprocessing.dummy import Pool as ThreadPool<br/>
<br/>
import json<br/>
import threading<br/>

### Bugs
Do not create netmiko.py file in the same directory.<br/>

