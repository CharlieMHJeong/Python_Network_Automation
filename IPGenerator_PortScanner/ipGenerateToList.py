import ipaddress
from termcolor import colored

try:
    from IPCalc import IPCalc

except:

    print("IPCalc.py does not exist!!")
    exit(1)

#Generate IP list from the Given Network address
def ip_generate_to_list():

    ip_list = []

    while True:
        net = input("Please enter a network address(IPAddress/sm): ")
        try:
            if "/" not in net:
                print(colored("Please enter a VALID IPAddress / sm", 'red'))
                continue
            else:
                ipaddr, sm = net.split("/")
                try:
                    valid = ipaddr.split(".")
                except:
                    print(colored("Please enter a VALID IP Address", 'red'))
                if int(sm) > 32 or int(sm) < 0:
                    print(colored("The VALID SM Range is [ 1 - 32 ]", 'red'))
            ipaddress.ip_network(net, strict=False)
            break

        except ValueError:
            print(colored("Please enter a VALID IP Network Address with sm", 'red'))

    print(IPCalc(net))
    addr = IPCalc(net)
    fst = addr[3]
    lst = addr[4]

    lst1 = []
    lst2 = []
    indxBool1 = False
    indxBool2 = False
    indx = 0
    try:
        for i, j in zip(fst, lst):
            if i == j:
                indx += 1
            else:
                if indx ==1 :
                    for octet in range(int(i), int(j) + 1):
                        indxBool1 = True
                        lst1.append(octet)
                    indx += 1
                elif indx == 2:
                    for octet in range(int(i), int(j) + 1):
                        indxBool2 = True
                        lst2.append(octet)
                    indx += 1
                elif indx == 3:
                    if indxBool1 is True:
                        genindx =1
                    elif indxBool2 is True:
                        genindx =2
                    else:
                        genindx = indx
                    if genindx ==1:
                        for octet in lst1:
                            for octet2 in lst2:
                                for octet3 in range(int(i), int(j) + 1):
                                    ip_list.append(".".join([str(p) for p in fst[0:genindx]]) + ".{}.{}.{}".format(octet, octet2, octet3))
                        del lst1
                    elif genindx == 2:
                        for octet in lst2:
                            for octet2 in range(int(i), int(j) + 1):
                                ip_list.append(".".join([str(p) for p in fst[0:genindx]]) + ".{}.{}".format(octet, octet2))
                        del lst2
                    else:
                        for octet in range(int(i), int(j) + 1):
                            ip_list.append(".".join([str(p) for p in fst[0:genindx]]) + ".{}".format(octet))
                else:
                    pass
                    # print(" [+] Done")
        return ip_list

    except KeyboardInterrupt:
        print("User hit CTRL+c")
        exit(1)
