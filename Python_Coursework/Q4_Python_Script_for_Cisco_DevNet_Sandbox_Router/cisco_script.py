from scrapli.driver.core import IOSXEDriver
# there is one library we used in this program "scrapli"
# The router I use is Cisco DevNet Sandbox IOS XE on CSR Latest Code (Always On)
# So we import IOSXEDriver to configure this router
# NXOSDriver for Cisco NX-OS
# IOSXRDriver for Cisco IOS-XR
# JunosDriver for Juniper JUNOS
# EOSDriver for Arista EOS

MY_DEVICE = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "port": 22,
    "auth_strict_key": False
}
# I configure the 'host', 'username', and 'password' from that the Cisco Sandbox provided
# port is 22, which is default
# auth_strict_key is False, which is default

lst = []  # create a list for the result of response (show run), and append this list to 'run.txt'

'''conn = IOSXEDriver(**MY_DEVICE)
conn.open()
response = conn.send_command("show ip interface brief")
print(response.result)
conn.close()'''


with IOSXEDriver(**MY_DEVICE) as conn:
    # "*" "**" for the unknown all the parameters
    # Because MY_DEVICE is a dictionary, so using "**" to unwrapped each element in MY_DEVICE and pass into the function as a key argument one by one
    # "*" for tuple
    response = conn.send_configs(
        ['interface gigabitethernet2',
         'ip address 192.168.12.1 255.255.255.0',
         'no shutdown', ]
    )
    # use "send_configs" to configure the router
    # the first step is to enter the configuration mode for  GigabitEthernet2 interface on the router
    # the second step is to set IP address and subnet mask for G2
    # enable this interface and change its state from administratively down to up.
    print(response.result)
    # print the result to show what is down

with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs(
        ['interface Loopback0',
         'ip address 10.108.1.1 255.255.255.0', ]
    )
    print(response.result)
    # use "send_configs" to configure the router
    # the first step is to enter the configuration mode for  loopback interface on the router
    # the second step is to set IP address and subnet mask for loopback interface


with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs(
        ['router rip',
         'version 2',
         'network 192.168.10.5',
         'no auto-summary', ]
    )
    print(response.result)
    # use "send_configs" to configure the router
    # the first step is to enables RIP on router
    # the second step is to specify use of RIP version 2
    # the third step is to specify a list of networks on which RIP is to be applied, using the address of the network of each directly connected network.
    # Disables automatic summarization of subnet routes into network-level routes. This allows subprefix routing information to pass across classful network boundaries.

with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs(
        ['router eigrp 109',
         'network 192.145.1.0', ]
    )
    print(response.result)
    # use "send_configs" to configure the router
    # the first step is to  enables EIGRP on the router.
    # 109 identifies the route to other EIGRP routers and is used to tag the EIGRP information.
    # the second step is to specify a list of networks on which EIGRP is to be applied,
    # using the IP address of the network of directly connected networks

with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs(
        ['router ospf 50',
         'network 50.50.50.50 0.0.0.0 area 50', ]
    )
    print(response.result)
    # the first step is to use the ospf protocol on all interfaces on this router in area 50.
    # the second step is to declare network segment 50.50.50.50, inverse code is0.0.0.0, ospf50 area is the backbone area.

with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_configs_from_file("config.txt")
    print(response.result)
    '''
    ntp server 14.14.14.14
    '''
    # to provide accurate practice
    # the address is the address of the time area


with IOSXEDriver(**MY_DEVICE) as conn:
    response = conn.send_command(
        'show run'
    )
    print(response.result)
    # will show the information of the router
    # version, service timestamps debug uptime, service timestamps log uptime, hostname, interface and it address and so on.

lst.append(str(response.result))
# append show run into the list, must for "string" type instead of response
f = open('run.txt', 'w')
# create a new txt 'run.txt', and enable to write
f.writelines(lst)
# write the list into it
f.close()
# close the file
