#SUBNET CALCULATOR
# - Display Subnet Information for a given IP and subnet mask
# - This uses ipaddress from the Python standard library

import argparse
import ipaddress

# statics
PROGRAMDESCRIPTION = 'Returns IP Information For Given IP and Subnet Mask'
HELPIPADDR = 'IPv4 address. Example: 192.168.1.100'
HELPSUBNETMASK = 'Subnet mask. Example: 255.255.255.0'

####################################
# returns network address if it checks out, raises an error if it fails.
def get_network_address(ipa, snm):

    ntwk_addr_int = int(ipaddress.IPv4Address(ipa)) & int(ipaddress.IPv4Address(snm))

    return str(ipaddress.ip_address(ntwk_addr_int)) + '/' + snm
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

    # ntwk is assigned class type ipaddress.IPv4Network
    ntwk = ipaddress.IPv4Network(get_network_address(clArgs.ipaddress, clArgs.subnetmask))
    
    # print to screen
    print(f'IPv4 Address: {clArgs.ipaddress}')
    print(f'Subnet Mask: {clArgs.subnetmask}')
    print(f'Host Mask: {ntwk.hostmask}')
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
