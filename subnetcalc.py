#SUBNET CALCULATOR
# - Display Subnet ID and Broadcast Address for a given IP and subnet mask

import argparse
import re
import sys

#statics
PROGRAMDESCRIPTION = 'Returns Subnet ID and Broadcast Address'
HELPIPADDR = 'IPv4 address in the following format: xxx.xxx.xxx.xxx'
HELPSUBNETMASK = 'subnet mask in the following format: xxx.xxx.xxx.xxx'
HELPVERBOSEOUTPUT = 'outputs descriptions'
ERRORINVALIDINPUT = 'Error: Invalid Input'
VERBOSESUBNET = 'Subnet ID is: '
VERBOSEBROADCAST = 'Broadcast Address is: '
VALIDSUBNETOCTETS = [0, 128, 192, 224, 240, 248, 252, 254]
####################################
def write_results(args, sid, bad):
    # parameters: command-line args, subnetId, broadcast adress

    # first checks to see if verbose output was requested
    if args.verbose:
        sid = VERBOSESUBNET + sid
        bad = VERBOSEBROADCAST + bad

    # output results
    print(sid)
    print(bad)

####################################
# calculates broadcast IP address as string, dotted decimal
# x is ip addr, y is subnet mask
def calc_broadcast_addr(x, y):

    bAddr = ''
    i = 0
    
    while i < 4:
        bAddr += str( (x[i] & y[i]) + (255 ^ y[i]) )
        if i != 3:
            bAddr += '.'
        i += 1

    return bAddr
####################################
# returns subnet ID as string, dotted decimal
def calc_subnet_id(x, y):

    subId = ''
    i = 0
    
    while i < 4:
        subId += str(x[i] & y[i])
        if i != 3:
            subId += '.'
        i += 1

    return subId
####################################
def valid_subnet_mask(x):
    interestingOctet = False

    # first octet must be 255
    if x[0] != 255:
        return False
    
    # second octet
    if x[1] != 255:
        if x[1] in VALIDSUBNETOCTETS:
            interestingOctet = True
        else:
            return False
    
    # third octet
    if interestingOctet:
        if x[2] != 0:
            return False
    elif x[2] != 255:
        if x[2] in VALIDSUBNETOCTETS:
            interestingOctet = True
        else:
            return False
    
    # fourth octet
    if interestingOctet:
        if x[3] != 0:
            return False
    elif x[3] not in VALIDSUBNETOCTETS or x[3] == 254:
        return False

    return True
####################################
# will loop by index since exception needs to be made
# for first octet. first octet cannot be zero.
# assumes ip format has been validated.
def valid_ip_addr(x):    
    i = 0
    if x[i] > 255 or x[i] == 0:
        return False
    
    i += 1

    while i < 4:
        if x[i] > 255:
            return False
        i += 1

    return True
####################################
# assumes that x has already been validated as a correct
# ip format
def convert_to_list(x):
    octetsInt = []
    octetsStr = x.split('.')
    for octet in octetsStr:
        octetsInt.append(int(octet))

    return octetsInt
####################################
# this only checks to ensure that the IP is correct x.x.x.x format
def valid_ip_format(x):
    if re.search('^(\d{1,3}\.){3}\d{1,3}$', x):
        return True
    else:
        return False
####################################
def get_arguments():
    parser = argparse.ArgumentParser(description=PROGRAMDESCRIPTION)
    parser.add_argument('-v', '--verbose', help=HELPVERBOSEOUTPUT, action='store_true')
    parser.add_argument('ipaddress', help=HELPIPADDR)
    parser.add_argument('subnetmask', help=HELPSUBNETMASK)
    
    return parser.parse_args()
####################################
def start_subnet_calc():

    # get command line arguments
    clArgs = get_arguments()

    # ensure inputs are in correct x.x.x.x format
    if not(valid_ip_format(clArgs.ipaddress)) or not(valid_ip_format(clArgs.subnetmask)):
        print(ERRORINVALIDINPUT)
        sys.exit(1)
    
    # change from single string to list of integers
    ipOctets = convert_to_list(clArgs.ipaddress)
    subnetOctets = convert_to_list(clArgs.subnetmask)

    # ensure ip addr and subnet mask numbers are valid
    if not(valid_ip_addr(ipOctets)) or not(valid_subnet_mask(subnetOctets)):
        print(ERRORINVALIDINPUT)
        sys.exit(1)
    
    # return subnet ID and broadcast addr as strings, dotted decimal format
    subnetId = calc_subnet_id(ipOctets, subnetOctets)
    broadcastAddr = calc_broadcast_addr(ipOctets, subnetOctets)

    # writes results to output
    write_results(clArgs, subnetId, broadcastAddr)

####################################
# MAIN
start_subnet_calc()