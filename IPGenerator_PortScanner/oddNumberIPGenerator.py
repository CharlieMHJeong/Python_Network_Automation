import ipGenerateToList

def odd_number_ip_generator():

    ip_list = ipGenerateToList.ip_generate_to_list()
    ip_list_odd = []
    for ip in ip_list:
        octets = ip.split('.')
        if int(octets[3]) % 2 == 0:
            continue
        else:
            ip_list_odd.append(ip)

    return ip_list_odd
