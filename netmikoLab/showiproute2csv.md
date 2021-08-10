#Show IP Route

Template took from:
https://github.com/networktocode/ntc-templates/blob/master/ntc_templates/templates/cisco_ios_show_ip_route.textfsm


### The command output
./showiproute2csv.py 
    PROTOCOL    TYPE    NETWORK      MASK  DISTANCE    METRIC    NEXTHOP_IP    NEXTHOP_IF           UPTIME
--  ----------  ------  ---------  ------  ----------  --------  ------------  -------------------  --------
 0  S                   1.1.1.1        32  1           0         212.0.0.1
 1  S                   1.1.1.1        32  1           0         192.168.0.1
 2  S                   2.2.2.0        24                                      FastEthernet0/0.100
 3  O           E2      4.4.0.0        16  110         20        194.0.0.2     FastEthernet0/0.100  1d18h
 4  D           EX      5.5.5.0        24  170         2297856   10.0.1.2      Serial0/0            00:12:01
