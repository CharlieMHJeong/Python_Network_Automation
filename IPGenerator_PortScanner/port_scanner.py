#!/bin/python3

import sys
import socket
from termcolor import colored
from datetime import datetime
import logging

logger = logging.getLogger('Port Scan Application CJ')
logger.setLevel(logging.DEBUG)

#create file handler with logs even debug messages
fh = logging.FileHandler('ip_port_log.txt')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def port_scanner(target, port):
    """
    Check port status
    :param target: IP Address as str
    :param port:  Port number as int
    :return:
    """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result = s.connect_ex((target,port)) #returns an error indicator
        #print("Checking port {}".format(port))
        if result == 0:
            # print(colored("\tPort {} : Open".format(port), attrs=['bold']))
            logger.info("\tPort {} : Open".format(port))
        else:
            # print("\tPort {} : Closed".format(port))
            logger.info("\tPort {} : Closed".format(port))
        s.close()

    except KeyboardInterrupt:
        # print("\nExting Program!!")
        logger.info("\nExting Program!!")
        sys.exit()

    except socket.gaierror:
        # print("Hostname could not be resolved")
        logger.info("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        # print("Could not connect to the server")
        logger.info("Could not connect to the server")
        sys.exit()
