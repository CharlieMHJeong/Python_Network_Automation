from netmiko import ConnectHandler

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'cisco',
	'password': 'cisco',
	}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.83',
	'username': 'cisco',
	'password': 'cisco',
	}

iosv_l2_s4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.84',
	'username': 'cisco',
	'password': 'cisco',
	}

iosv_l2_s5 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.85',
	'username': 'cisco',
	'password': 'cisco',
	}

iosv_l2_s6 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.86',
	'username': 'cisco',
	'password': 'cisco',
	}

with open('iosv_l2_cisco_access') as f:
	lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
	print(output)


with open('iosv_l2_cisco_core') as f:
	lines = f.read().splitlines()
print(lines)

all_devices = [iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6 ]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
	print(output)