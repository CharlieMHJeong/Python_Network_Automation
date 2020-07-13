from simplecrypt import encrypt, decrypt
from pprint import pprint
import csv
import json


#---- Read in pertinent information from user
#create 'device-creds' file as below: 
#192.168.122.72,cisco,cisco
#192.168.122.73,cisco,cisco
#192.168.122.74,cisco,cisco
#192.168.122.75,cisco,cisco
dc_in_filename = input('\nInput CSV filename (device-creds) : ') or 'device-creds'
key            = input('Encryption key (cisco) ') or 'cisco'

#---- Read in the device credentials from CSV file into list of device credentials
with open(dc_in_filename, 'r') as dc_in:
    device_creds_reader = csv.reader(dc_in)
    device_creds_list = [ device for device in device_creds_reader]

print("\n ----- device_creds -------------------------------------------------")
pprint(device_creds_list)

#---- Encrypt the device credentials using ken from user
encrypted_dc_out_filename = input('\nOutput encrypted filename (encrypted-device-creds): ') or 'encrypted-device-creds'

with open(encrypted_dc_out_filename, 'wb') as dc_out:
    dc_out.write(encrypt(key, json.dumps(device_creds_list)))

print("I have encrypted the file")

with open(encrypted_dc_out_filename, 'rb') as dc_in:
    device_creds_in = json.loads(decrypt(key, dc_in.read()))

print("\n---- confirm: device_creds json in ----------------------------------")
pprint(device_creds_in)
