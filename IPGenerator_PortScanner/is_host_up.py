import os
import platform

def ping(host):
    """
    use Ping to check whether the host is up or down.
    :param host:
    :return: host status as Boolean
    """
    res = False

    ping_param = "-n 1" if platform.system().lower() == "windows" else "-c 1"

    resultado = os.popen("ping " + ping_param + " " + host).read()

    if "TTL=" in resultado:
        res = True
    else:
        res = False
    return res
