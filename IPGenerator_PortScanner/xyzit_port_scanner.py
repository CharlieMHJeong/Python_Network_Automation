import logging

import xyzit_ipgenerator
import is_host_up
import port_scanner
import writingToEventViewer


def import_portfile():
    with open('ports.txt','r') as p:
        l = p.readlines()
    port_list = [line.rstrip() for line in l]
    return  port_list

def ip_generator():
    ip_list = xyzit_ipgenerator.xyzit_ipgenerator()
    return ip_list

def check_host_up(host):
    """
    Checking host status
    :param host:
    :return:  host status as Boolean
    """
    result = is_host_up.ping(host)
    return result



def main():

    # ip_list = ['192.168.47.140','192.168.47.141', '192.168.47.142', '192.168.47.143']
    # 192.168.47.128/26
    # 192.168.47.128/28

    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0

    #create logger with "IP Scan Application by CJ"

    logger = logging.getLogger('IP Scan Application CJ')
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

    ip_list = ip_generator()
    # print(ip_list)
    port_list = import_portfile()

    for host in ip_list:
        logger.info("Scanning {}".format(host))
        if check_host_up(host) is False:
            logger.info("{}: Not Available ".format(host))
        else:
            logger.info("+"*50)
            logger.info("{}: UP".format(host))
            logger.info("Port Scanning for {}".format(host))
            for port in port_list:
                port_scanner.port_scanner(host, int(port))
            logger.info("+"*50)

    #Writing to windows eventviewer
    writingToEventViewer.write_to_eventviewer(ip_list)

    # with open('ip_port_log.txt', 'w') as f:
    #     for host in ip_list:
    #         print("Checking {}".format(host))
    #         f.write("Checking {}".format(host), "\n")
    #         if check_host_up(host) is False:
    #             print("Host {}: Not Available ".format(host))
    #         else:
    #             print("+"*50)
    #             print(colored("Host {}: UP".format(host), attrs=['bold']))
    #             for port in port_list:
    #                 port_scanner.port_scanner(host, int(port))
    #             print("+"*50)

main()
