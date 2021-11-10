# IPGenerator_PortScanner

## Getting Started
This application is going to generate IPs from the given network and scan ports(ports.txt).

### System requirement
Please install python 3.7.4 and run it on Windows.

### Feature Requirement
1.	All IP addresses generated must fall within the subnet input by the end-user <br/>
    •	the end-user will be prompted to provide the subnet and subnet mask when the script first starts <br/>
    •	for example: subnet 192.168.x with subnet mask of 255.255.255.0 <br/>
2.	The script must skip every IP address that is evenly numbered (divisible by 2) <br/>
    •	for example: 192.168.0.12, 192.168.0.14, … , 192.168.0.252, 192.168.0.254 
3.	Reserves the top 10 IP addresses for printers and servers 
4.	scan all ports for each of the IP addresses in the subnet  <br/>
    •	the ports are defined a file (ports.txt) that is imported when the script starts  <br/>
    •	outputs the status of each port (open or closed) 
5.	the script must output the IP address and port status to: <br/>
    •	console <br/>
    •	log file (ip_port_log.txt)<br/>
    •	Windows Event Viewer (IP Addresses Only)<br/>

### Running the tests
1.	Put all the files in the same directory 
2.	Please prepare ports.txt file 
3.	Run “xyzit_port_scanner.py” 
4.	Enter proper IP network address when it prompts<br/>
    •	Please enter a network address(IPAddress/sm):
5.	Please check console or ip_port_log.txt file for the result.

### EventViewer in Windows
Use writingToEventViewer.py to modify the EventID, CategoryID and EventType <br/>

EventID: 7040<br/>
CategoryID: 9876<br/>
EventType:<br/>
    EVENTLOG_ERROR_TYPE : Error Level<br/>
    EVENTLOG_WARNING_TYPE: Warning Level<br/>


### Imported Libraries
1.	ipaddress
2.	os
3.	platform
4.	socket
5.	logging
6.	win32evtlogutil
7.	win32evtlog
8.	time
9.	logging
10.	sys


### Bug Fixes:

### Release Notes:
#1.0.0 - CJ 29.05.2020 First draft
