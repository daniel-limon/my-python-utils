#SUBNET CALCULATOR
# - Display Subnet Information for a given IP and subnet mask
# - This uses ipaddress from the Python standard library

import argparse
import ipaddress
import sys

# statics
PROGRAMDESCRIPTION = 'Returns Subnet Information For Given IP and Subnet Mask'
HELPIPADDR = 'IPv4 address. Example: 192.168.1.100'
HELPSUBNETMASK = 'Subnet mask. Example: 255.255.255.0'

####################################
# this validates the ip address and subnet mask.
# returns network address if it checks out, false if it fails
def get_network_address(ipa, snm):

    # this will catch error if there is an illegal octet,
    # or an improperly formatted ipv4 address.
    try:
        # calculate network address
        ntwk_addr_int = int(ipaddress.IPv4Address(ipa)) & int(ipaddress.IPv4Address(snm))
    except:
        return 'False'

    # converts network address from type int to type str
    ntwk_addr = str(ipaddress.ip_address(ntwk_addr_int)) + '/' + snm

    # this will catch error if the subnet mask is invalid
    try:
        ipaddress.IPv4Network(ntwk_addr)
    except:
        return 'False'
    
    # return address string if values are good
    return ntwk_addr
####################################
# command-line parser
def get_arguments():
    parser = argparse.ArgumentParser(description=PROGRAMDESCRIPTION)
    parser.add_argument('ipaddress', help=HELPIPADDR)
    parser.add_argument('subnetmask', help=HELPSUBNETMASK)
    
    return parser.parse_args()
####################################
def start_subnet_calc():

    # get command line arguments
    clArgs = get_arguments()

    # validates good ip address and subnet mask
    network_address = get_network_address(clArgs.ipaddress, clArgs.subnetmask)
    if network_address == 'False':
        print('Invalid IP and/or subnet mask')
        exit(1)

    # ntwk is assigned class type ipaddress.IPv4Network
    ntwk = ipaddress.IPv4Network(network_address)
    
    # print to screen
    print(f'IPv4 Address: {clArgs.ipaddress}')
    print(f'Subnet Mask: {clArgs.subnetmask}')
    print(f'Network Address: {ntwk.network_address}')
    print(f'Network Address with CIDR: {ntwk.network_address}/{ntwk.prefixlen}')
    print(f'First Assignable IP: {ntwk.network_address + 1}')
    print(f'Last Assignable IP: {ntwk.broadcast_address - 1}')
    print(f'Broadcast Address: {ntwk.broadcast_address}')
    print(f'Number of Total IPs in Subnet: {ntwk.num_addresses}')
    print(f'Number of Assignable Addresses: {ntwk.num_addresses - 2}')
    print(f'Private Address: {ntwk.is_private}')
    print(f'Reserved Address: {ntwk.is_reserved}')
    print(f'Loopback Address: {ntwk.is_loopback}')

####################################
# MAIN
start_subnet_calc()