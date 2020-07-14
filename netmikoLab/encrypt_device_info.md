#Encrypt Login Credentials

## Getting Started
This application is going to encrypt the provided csv file.

### System requirement
1. simple-crypt installing on Ubuntu:
 • apt-get update
 • apt-get install python3-pip
 • apt-get install python3.8-dev
 • pip3 install pycryptodome
 • pip3 install simple-crypt

2. CSV file without Header. IP, ID, PW:
192.168.122.72,cisco,cisco
192.168.122.73,cisco,cisco
192.168.122.74,cisco,cisco
192.168.122.75,cisco,cisco


### Run it
Put the CSV file on the same directory and run the py file.
Encrypted file "encrypted-device-creds" will be created at the same directory.
