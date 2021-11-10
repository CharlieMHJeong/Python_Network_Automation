import sys
import win32evtlogutil
import win32evtlog
import time

def write_to_eventviewer(iplist):
    """
    Write to Windows EventViewer
    :param iplist:
    :return:
    """

    "Python {:s} on {:s}".format(sys.version, sys.platform)
    #example IP addresses, your script will need to dynamically generate these address, this collection has only
    # ip_addresses = ['192.168.0.12','192.168.0.14','192.168.0.16','192.168.0.18','192.168.0.20','192.168.0.22']
    ip_addresses = iplist
    DUMMY_EVT_APP_NAME = "IP Scan Application CJ"
    DUMMY_EVT_ID = 7040
    DUMMY_EVT_CATEG = 9876
    DUMMY_EVT_STRS = ["IP: {:s}".format(ip) for ip in ip_addresses]
    DUMMY_EVT_DATA = b"Scan IP Address Event Data"
    "Current time: {:s}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    win32evtlogutil.ReportEvent(DUMMY_EVT_APP_NAME,
                                DUMMY_EVT_ID,
                                eventCategory=DUMMY_EVT_CATEG,
                                eventType=win32evtlog.EVENTLOG_WARNING_TYPE,
                                strings=DUMMY_EVT_STRS,
                                data=DUMMY_EVT_DATA)
