
root@NetworkAutomation-1:~/pythonlab# python3 scanner.py 192.168.200.254
--------------------------------------------------
scanning target 192.168.200.254
Time started: 2021-08-11 11:48:20.641636
--------------------------------------------------
The port 53 is open
The port 80 is open
--------------------------------------------------
Time Finished: 2021-08-11 11:48:23.697082
--------------------------------------------------


root@NetworkAutomation-1:~/pythonlab# cat scanner.py
#!/usr/bin/python3

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
    #hostname to IPv4
    #set the 1st arg as target
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid ARGs")
    print("Syntax: python3 scanner.py <ip>")

#Adding a banner
print('-' *50)
print("scanning target " + target)
print("Time started: " + str(datetime.now()))
print('-' *50)

try:
    for port in range(50,85):
        #AF_INET: IPv4, SOCK_STREAM: port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("The port {} is open".format(port))
        #else:
        #    print("The port {} is NOT open".format(port))
        s.close()
except KeyBoardInterrupt:
    print("\n Exting ")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to the server")
    sys.exit()

except Exception as e:
    print(e)
    sys.exit()

#Adding a banner
print('-' *50)
print("Time Finished: " + str(datetime.now()))
print('-' *50)

root@NetworkAutomation-1:~/pythonlab#
