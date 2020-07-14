# Read Configs from Cisco Device with MultiThreading

## Getting Started
This application is going to read cisco device configurations.

### Requirements
1. Create 'encrypted-device-creds' encrypted login credential file from "encrypt_device_info.py"
2. CSV file 'devices-file' with IP, DeviceType, Hostname
   • 192.168.122.72, cisco-ios, S1
   • 192.168.122.73, cisco-ios, S2
   • 192.168.122.74, cisco-ios, R1
   • 192.168.122.75, cisco-ios, R2

### How To in Linux
1. python3 read_config_threadingpool.py
2. When prompted, enter number of threads that your system can support
   Number of thread(s) (5):
3. Check the config-files:
•-rw-r--r-- 1 root root 4056 Jul 14 10:49 config-192.168.122.72
•-rw-r--r-- 1 root root 4040 Jul 14 10:49 config-192.168.122.73
•-rw-r--r-- 1 root root 3382 Jul 14 10:49 config-192.168.122.74
•-rw-r--r-- 1 root root 3383 Jul 14 10:49 config-192.168.122.75


### Imported Libraries
• from simplecrypt import encrypt, decrypt
• from pprint import pprint
• from netmiko import ConnectHandler
• from multiprocessing.dummy import Pool as ThreadPool

• import json
• import threading
